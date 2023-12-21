import googleapiclient.discovery
import pandas as pd

api_service_name = "youtube"
api_version = "v3"
API_KEY = "AIzaSyASfwtKSfUAAGR6DUM0dhmx48AfbZo1MzY"

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=API_KEY)

request = youtube.commentThreads().list(
    part="snippet",
    videoId="CSPvynsXa4I",   # Tekken8 trailer
    maxResults=100
)
response = request.execute()

comments = []

print(response)

for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']
    comments.append([
        comment['authorDisplayName'],
        comment['publishedAt'],
        comment['updatedAt'],
        comment['likeCount'],
        comment['textDisplay']
    ])

df = pd.DataFrame(comments, columns=['author', 'published_at', 'updated_at', 'like_count', 'text'])

df.to_csv(f"../../data/raw/comments.csv")

print(df.head(10))