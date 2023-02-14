import os
from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('AIzaSyDDVPXfBre2oshFEgqCh2NjQz9AQXmb10U')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

import json

# channel_id = '"UCByhZ-JEe5OOZSuq0uaXOng"'  # Нежный редактор
channel_id = '"UCByhZ-JEe5OOZSuq0uaXOng"'

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Youtube:
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def get_service(self):
        service = youtube   # build('youtube', 'v3', developerKey=api_key)
        return service

    def get_channel_info(channel_id):
        r = get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        print(r['items'][0]['snippet']['title'])
        print(r['items'][0]['statistics']['viewCount'])


