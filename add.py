import requests
import sys
import time
from pathlib import Path
import mimetypes
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    TOKEN = os.getenv('SLACK_PRIVATE_TOKEN')
    WORKSPACE = os.getenv('SLACK_WORKSPACE_NAME')

    for line in iter(sys.stdin.readline, ""):
        p = Path(line.rstrip())
        name = p.stem
        mime_type = mimetypes.guess_type(p)[0]
        img_data = open(p, 'rb').read()

        data = {"name": (None, name, ""), "mode": (None, "data", ""), "token": (
            None, TOKEN, ""), "image": (p.name, img_data, mime_type)}
        print(name)

        response = requests.post(
            f'https://{WORKSPACE}.slack.com/api/emoji.add', files=data)
        print(response.json())

        time.sleep(3)


if __name__ == '__main__':
    main()
