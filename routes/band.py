import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

band_token = os.getenv('BAND_TOKEN')
band_key = os.getenv('BAND_KEY')


# Get Post
def get_post():
    get_post_url = 'https://openapi.band.us/v2/band/posts'

    return json.loads(requests.get(
        get_post_url,
        params={
            'access_token': band_token,
            'band_key': band_key,
            'locale': 'en_GB'
        }
    ).content)


# Write Post
def write_post(post_content):
    write_post_url = 'https://openapi.band.us/v2.2/band/post/create'

    requests.post(
        write_post_url,
        params={
            'access_token': band_token,
            'band_key': band_key,
            'content': post_content
        }
    )


# Write Comments
def write_comment(comment_body, post_key):
    write_comment_url = 'https://openapi.band.us/v2/band/post/comment/create'

    requests.post(
        write_comment_url,
        params={
            'access_token': band_token,
            'band_key': band_key,
            'post_key': post_key,
            'body': comment_body
        }
    )
