import os
from googleapiclient.discovery import build

#from dotenv import load_dotenv

#load_dotenv()
YOUTUBE_KEY = "AIzaSyDDVPXfBre2oshFEgqCh2NjQz9AQXmb10U"
# API_KEY = os.getenv('YOUTUBE_KEY')
API_KEY = YOUTUBE_KEY


class Youtube:
    channel_id = "UCByhZ-JEe5OOZSuq0uaXOng"
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def __init__(self, channel_id, channel_name, channel_description, hm_followers, hm_videos, hm_views):
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.channel_description = channel_description
        self.hw_followers = hm_followers
        self.hw_videos = hm_videos
        self.hm_views = hm_views
        self.channel_info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def get_service(self):
        service = youtube  # build('youtube', 'v3', developerKey=api_key)
        return service

    def get_channel_info(channel_id):
        r = get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        print(r['items'][0]['snippet']['title'])
        print(r['items'][0]['statistics']['viewCount'])

    def print_info(self):
        return self.channel_info

    if __name__ == "__main__":
        print_info()
