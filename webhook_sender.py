import requests
import json
import argparse

"""
Send a webhook with a simple message to the default (local Flask development server) or 
enter the URL to the specified webserver receiver
"""

# Local Flask server
DEFAULT_WEBHOOK_URL = r"http://127.0.0.1:5000/webhook" 

def choose_url():
    argparser = argparse.ArgumentParser(description=__doc__)

    argparser.add_argument(
        '-u','--url',
        type=str,
        default=DEFAULT_WEBHOOK_URL,
        help="Set the URL to the specified webhook server"
    )

    args = argparser.parse_args()
    return args

dummy_data = {
    "from": "Mr Gallas",
    "content": "Hello world!"
}

if __name__ == '__main__':
    chosen_url = choose_url()
    requests.post(url=chosen_url.url, data=json.dumps(dummy_data), headers={"Content-Type":'applications/json'})