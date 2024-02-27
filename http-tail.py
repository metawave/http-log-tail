import requests
import argparse
import time
import sys
from requests.exceptions import HTTPError, ConnectionError

parser = argparse.ArgumentParser(description='Monitor changes to a log file over HTTP.')
parser.add_argument('url', type=str, help='The URL of the log file to monitor.')
parser.add_argument('--user', type=str, help='The username for Basic Auth.', default=None)
parser.add_argument('--password', type=str, help='The password for Basic Auth.', default=None)
parser.add_argument('--interval', type=int, help='Polling interval in seconds.', default=5)

args = parser.parse_args()

file_url = args.url
username = args.user
password = args.password
interval = args.interval

last_size = 0

s = requests.Session()

# Set Basic Auth credentials if provided
if username and password:
    s.auth = (username, password)

while True:
    response = None

    try:
        response = s.head(file_url)
        if not response.ok:
            response.raise_for_status()

        content_length = int(response.headers.get('Content-Length', 0))

        if content_length > last_size:
            headers = {"Range": f"bytes={last_size}-"}
            response = s.get(file_url, headers=headers)
            print(response.text, end='')

            last_size = content_length

    except (ConnectionError, HTTPError) as e:
        print(e, file=sys.stderr)
    finally:
        if response is not None:
            response.close()

    time.sleep(interval)  # Poll every x seconds
