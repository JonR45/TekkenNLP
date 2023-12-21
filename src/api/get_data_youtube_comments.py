# get_youtube_comments.py
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def get_channel_videos_info(API_KEY, channel_id, published_after, published_before,):
    youtube = build('youtube', 'v3', developerKey={API_KEY})

    video_data = []
    next_page_token = None

    while True:
        # Make a request for videos in the desired channel and date range
        request = youtube.search().list(
            part='snippet',
            order='date',
            publishedAfter=published_after,   # .isoformat('T00:00:00Z'),
            publishedBefore=published_before,   #.isoformat('T23:59:59Z'),
            type='video',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        # Extract video information from search results
        for item in request['items']:
          video_info = {
              'videoId': item['id']['videoId'],
              'title': item['snippet']['title'],
              'description': item['snippet']['description'],
              'viewCount': None,
              'likeCount': None,
              'commentCount': None,
          }

          # Get additional details using videos().list
          additional_info = youtube.videos().list(
              part='statistics',
              id=video_info['videoId']
          ).execute()

          # Update video information with statistics
          if additional_info.get('items'):
              video_info.update({
                  'viewCount': additional_info['items'][0]['statistics'].get('viewCount'),
                  'likeCount': additional_info['items'][0]['statistics'].get('likeCount'),
                  'commentCount': additional_info['items'][0]['statistics'].get('commentCount')})

        video_data.append(video_info)

        # Check if there are more pages of results
        next_page_token = request.get('nextPageToken')
        if not next_page_token:
          break

    return video_data



def get_video_comments(video_id):
    youtube = build('youtube', 'v3', developerKey={API_KEY})

    comments = []
    next_page_token = None

    while True: # Make a request for comments with replies
        request = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        # Extract comment data from response
        for item in request['items']:
            comment = {
                'authorDisplayName': item['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                'textDisplay': item['snippet']['topLevelComment']['snippet']['textDisplay'],
                'publishedAt': item['snippet']['topLevelComment']['snippet']['publishedAt'],
                'replies': []
            }

            # Add replies if available
            if item['replies']['pageInfo']['totalResults']:
                for reply in item['replies']['items']:
                    comment['replies'].append(
                        {
                        'authorDisplayName': reply['snippet']['authorDisplayName'],
                        'textDisplay': reply['snippet']['textDisplay'],
                        'publishedAt': reply['snippet']['publishedAt'],
                        }
                    )

            comments.append(comment)

        # Check if there are more pages of results
        next_page_token = request.get('nextPageToken')
        if not next_page_token:
            break

    return comments
