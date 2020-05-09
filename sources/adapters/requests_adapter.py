import os

import requests
from dotenv import load_dotenv


class RequestsAdapter:
    def __init__(self):
        load_dotenv()

    def http_get(self, uri: str, payload=None) -> dict:
        params = {'api_key': os.getenv('API_KEY')}
        if payload is not None:
            params = {**{'api_key': os.getenv('API_KEY')}, **payload}
        request = requests.get(f"{os.getenv('API_BASE_URL')}{uri}",
                               params=params)
        return {
            'url': request.url,
            'status_code': request.status_code,
            'json': request.json()
        }
