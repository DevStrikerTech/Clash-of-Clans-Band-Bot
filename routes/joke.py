import requests
import json


def get_random_joke():
    joke_request_url = 'https://official-joke-api.appspot.com/random_joke'
    return json.loads(requests.get(joke_request_url).content)
