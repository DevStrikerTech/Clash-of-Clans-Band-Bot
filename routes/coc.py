import urllib.request
import json
from dotenv import load_dotenv
import os

load_dotenv()

coc_key = os.getenv('COC_TOKEN')


def coc_request(coc_endpoint):
    coc_request_url = 'https://api.clashofclans.com/v1'

    coc_response = urllib.request.Request(
        coc_request_url + coc_endpoint,
        None,
        {
            'Authorization': 'Bearer %s' % coc_key
        }
    )

    return json.loads(urllib.request.urlopen(coc_response).read().decode('utf-8'))
