# get_youtube_data.py
"""Module contains functions that connect to the YouTube API and retrieve video data.

Functions include:
    `get_video_ids(youtube_service_object, channel_id: str, published_after, published_before, search_term: str = None)`
    `get_video_data(video_ids)`
    `get_top_level_comments(youtube_service_object, video_ids)`

"""

import googleapiclient.discovery
import pandas as pd
from tqdm.notebook import tqdm


def get_video_ids(youtube_service_object, channel_id: str, published_after, published_before, search_term: str = None):
    """Connects to the YouTube Data API using 'search' and returns video Ids for a specified request.

    
    Parameters
    ----------
    youtube_service_object : googleapiclient object
        a service object created using `googleapiclinet.discovery.build`

    channel_Id : str
        The id of the YouTube channel you want to search for videos.

    published_after : datetime
        an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).

    published_before : datetime
        an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).

    query : str
        A search term if you wish to narrow down the search using keywords. See Notes for 
        further information.



    Returns
    --------
    video_ids : list
        A list of the videoId values obtained from the request.

    
    Notes
    ------
    query : str
        Your request can also use the Boolean NOT (-) and OR (|) operators to exclude videos or 
        to find videos that are associated with one of several search terms. For example, to 
        search for videos matching either "boating" or "sailing", set the q parameter value to 
        boating|sailing. Similarly, to search for videos matching either "boating" or "sailing" 
        but not "fishing", set the q parameter value to boating|sailing -fishing. Note that the 
        pipe character must be URL-escaped when it is sent in your API request. The URL-escaped 
        value for the pipe character is %7C.


    References
    -----------
        https://developers.google.com/youtube/v3/docs/search
    
    """
    
    # make a request to the youtube api
    request = youtube_service_object.search().list(
        channelId=channel_id,
        publishedAfter=published_after,
        publishedBefore=published_before,
        q=search_term,
        part="snippet", 
        type="video",
        order="date",
        maxResults=50,
    )
    response = request.execute()
    
    video_ids = []

    # loop through response and store video Ids in a list
    for i, v in enumerate(range(len(response["items"]))):
        video_ids.append(response["items"][i]["id"]["videoId"])
    
    next_page_token = response.get("nextPageToken", None)
    more_pages = True
    
    while more_pages == True:
        if next_page_token is None:
            more_pages = False
    
        else: 
            # make a request to the youtube api to get the next page results
            request = youtube_service_object.search().list(
            channelId=channel_id,
            publishedAfter=published_after,
            publishedBefore=published_before,
            q=search_term,
            part="snippet", 
            type="video",
            order="date",
            maxResults=50,
            pageToken=next_page_token
            )
            response = request.execute()
    
            for i, v in enumerate(range(len(response["items"]))):
                video_ids.append(response["items"][i]["id"]["videoId"])
            
            next_page_token = response.get("nextPageToken", None)
    
    return video_ids



def get_video_data(youtube_service_object, video_ids):
    """Retrieves statistics for a given YouTube video ID and creates a dataframe with data for the
    videos that contain "tekken" in the title.

    Parameters
    ----------
    youtube_service_object : googleapiclient object
        a service object created using `googleapiclinet.discovery.build`
    
    video_ids : list or str
        A list of video IDs or a single string if only wanting to return data for one video ID.

    Returns
    --------
    df : dataframe
        A dataframe with the data for video Ids whose title contains the word "tekken".
    
    """

    all_data_dict = {}
    
    # split video_ids list into batches of 50 and process each batch using helper function
    for index, batch_start in tqdm(enumerate(range(0, len(video_ids), 50))):
        print(f"Batch {index+1} start: {batch_start}")
        batch_end = min(batch_start + 50, len(video_ids))
        print(f"Batch {index+1} end: {batch_end}")
        batch_ids = video_ids[batch_start:batch_end]

        # get data for the batch of <=50 video ids using helper function
        batch_data = _get_video_data_for_batch(youtube_service_object, batch_ids)
        all_data_dict.update(batch_data)


    # create dataframe from dictionary data
    df = (pd.DataFrame.from_dict(all_data_dict, orient="index")
          .rename_axis("videoId")
          .astype({"publishedAt": "datetime64[ns, UTC]", 
                           "viewCount": "int64", 
                           "likeCount": "int64", 
                           "commentCount": "int64", 
                           "favoriteCount": "int64"})
          .drop_duplicates(subset=['videoId'])
          .sort_values(by=["publishedAt"])
          .reset_index(drop=True)
         )

    # add a line that drops rows where 'tekken' isn't in the video title
    df = (df.loc[df['title'].str.lower().str.contains("tekken")]
          .reset_index(drop=True))


    return df



def _get_video_data_for_batch(youtube_service_object, video_ids):
    """Helper function that retrieves statistics for a given YouTube video ID, in batches 
    of 50 video ids at a time.

    Parameters
    ----------
    youtube_service_object : googleapiclient object
        a service object created using `googleapiclinet.discovery.build`
    
    video_ids : list or str
        A list of video IDs or a single string if only wanting to return data for one video ID.

    Returns
    -------
    data_dict : dictionary
        A dictionary with the data for the passed video IDs.
    
    """
 
    request = youtube_service_object.videos().list(
        part="snippet,statistics",
        maxResults=50,
        id=video_ids
    )
    
    response = request.execute()
    
    data_dict = {}
    
    # loop through response and store data about each video in a dictionary
    for i, v in enumerate(response["items"]):
        data_dict_ = {
            response["items"][i]["id"]: {"channelTitle": response["items"][i]["snippet"]["channelTitle"],
                                         "channelId": response["items"][i]["snippet"]["channelId"],
                                         "videoId": response["items"][i]["id"],
                                         "publishedAt": response["items"][i]["snippet"]["publishedAt"],
                                         "title": response["items"][i]["snippet"]["title"],
                                         "description": response["items"][i]["snippet"]["description"],
                                         "tags": response["items"][0]["snippet"].get("tags"),   # use .get() so none is returned if 'tags' isn't present (video doesn't have tags)
                                         "viewCount": response["items"][i]["statistics"]["viewCount"],
                                         "likeCount": response["items"][i]["statistics"]["likeCount"],
                                         "commentCount": response["items"][i]["statistics"]["commentCount"],
                                         "favoriteCount": response["items"][i]["statistics"]["favoriteCount"],
                                        }
        }
        
        # add the data to the data dictionary
        data_dict.update(data_dict_)
    
    next_page_token = response.get("nextPageToken", None)
    more_pages = True
    
    while more_pages == True:
        if next_page_token is None:
            more_pages = False
    
        else: 
            # make a request to the youtube api to get the next page results   
            request = youtube_service_object.videos().list(
                part="snippet,statistics",
                maxResults=50,
                id=video_ids,
                pageToken=next_page_token,
            )
            
            response = request.execute()
                
            # loop through response and store data about each video in a dictionary
            for i, v in enumerate(response["items"]):
                data_dict_ = {
                    response["items"][i]["id"]: {"channelTitle": response["items"][i]["snippet"]["channelTitle"],
                                                 "channelId": response["items"][i]["snippet"]["channelId"],
                                                 "videoId": response["items"][i]["id"],
                                                 "publishedAt": response["items"][i]["snippet"]["publishedAt"],
                                                 "title": response["items"][i]["snippet"]["title"],
                                                 "description": response["items"][i]["snippet"]["description"],
                                                 "tags": response["items"][i]["snippet"].get("tags"),   # use .get() so none is returned if 'tags' isn't present (video doesn't have tags)
                                                 "viewCount": response["items"][i]["statistics"]["viewCount"],
                                                 "likeCount": response["items"][i]["statistics"]["likeCount"],
                                                 "commentCount": response["items"][i]["statistics"]["commentCount"],
                                                 "favoriteCount": response["items"][i]["statistics"]["favoriteCount"],
                                                }
                }
                
                # add the data to the data dictionary
                data_dict.update(data_dict_)
        
            next_page_token = response.get("nextPageToken", None)

    
    return data_dict




def get_top_level_comments(youtube_service_object, video_ids):
    """Retrieves the commentThreads for a given YouTube video ID or list of video IDs.

    Parameters
    ----------
    video_ids : list or str
        A list of video IDs or a single string if only wanting to return data for one video ID.

    Returns
    --------
    df : dataframe
        A dataframe with the top level comments for the video ID.
    
    """

    # check if the video_ids input is a single string or list
    if isinstance(video_ids, str):
        video_ids = [video_ids]
  
    
    comments = []
    
    # loop through the remaining video ids, get the comments for these videos
    for index, video_id in enumerate(video_ids): 
        # make a request for first video id
        request = youtube_service_object.commentThreads().list(
            part="snippet",
            videoId=video_id,  
            order="time",
            maxResults=50
        )
        
        response = request.execute()
        
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([
                comment['videoId'],
                comment['authorDisplayName'],
                comment['publishedAt'],
                comment['updatedAt'],
                comment['likeCount'],
                item['snippet']['totalReplyCount'], # reply count not stored in same section of json response as all the others        
                comment['textDisplay']
            ])
        
        next_page_token = response.get("nextPageToken", None)
        more_pages = True
            
        while more_pages == True:
            if next_page_token is None:
                more_pages = False
        
            else: 
                # make a request to the youtube api to get the next page results   
                request = youtube_service_object.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    order="time",
                    maxResults=50,
                    pageToken=next_page_token,
                )
                
                response = request.execute()
        
                # loop through response and store data about each video in a dictionary
                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']
                    comments.append([
                        comment['videoId'],
                        comment['authorDisplayName'],
                        comment['publishedAt'],
                        comment['updatedAt'],
                        comment['likeCount'],
                        item['snippet']['totalReplyCount'], # reply count not stored in same section of json response as all the others        
                        comment['textDisplay']
                    ])
        
                
                next_page_token = response.get("nextPageToken", None)         
    
        
        
        df = (pd.DataFrame(data=comments, columns=['videoId', 'authorDisplayName', 'publishedAt', 'updatedAt', 
                                                  'likeCount', 'totalReplyCount', 'textDisplay'])
                        .astype({"publishedAt": "datetime64[ns, UTC]", 
                                 "updatedAt": "datetime64[ns, UTC]", 
                                 "likeCount": "int64", 
                                 "totalReplyCount": "int64"})
                        .drop_duplicates(subset=["textDisplay"])
                        .sort_values(by=["publishedAt"])
                        .reset_index(drop=True)
                       )
    
    
    return df