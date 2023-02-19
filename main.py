import os
from googleapiclient.discovery import build

from dotenv import load_dotenv

load_dotenv()

# API_KEY = os.getenv('YOUTUBE_KEY')
API_KEY = os.environ.get('YOUTUBE_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=API_KEY)

import json

# channel_id = '"UCByhZ-JEe5OOZSuq0uaXOng"'  # Нежный редактор
channel_id = "UCByhZ-JEe5OOZSuq0uaXOng"

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


class Youtube:

    def __init__(self, channel_id):
        self.channel_id = channel_id
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



