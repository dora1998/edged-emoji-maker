import requests
import sys
import time
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    TOKEN = os.getenv('SLACK_PRIVATE_TOKEN')
    WORKSPACE = os.getenv('SLACK_WORKSPACE_NAME')

    for line in iter(sys.stdin.readline, ""):
        name = line.rstrip()
        data = {"name": (None, name, ""), "token": (None, TOKEN, ""),
                "_x_reason": (None, "customize-emoji-remove", ""), "_x_reason": (None, "customize-emoji-remove", "")}
        print(name)

        response = requests.post(
            f'https://{WORKSPACE}.slack.com/api/emoji.remove', files=data)
        print(response.json())

        time.sleep(3)


if __name__ == '__main__':
    main()
