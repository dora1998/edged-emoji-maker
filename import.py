import os
from time import sleep
import requests
from dotenv import load_dotenv


def download_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"HTTP Error: {response}")
        return None

    content_type = response.headers["content-type"]
    if 'image' not in content_type:
        print(f"Error: {content_type} is not image")
        return None

    return response.content


def make_filename(base_dir, alias, url):
    ext = os.path.splitext(url)[1]
    filename = alias + ext

    fullpath = os.path.join(base_dir, filename)
    return fullpath


def save_image(path, image):
    with open(path, "wb") as fout:
        fout.write(image)


def main():
    load_dotenv()
    TOKEN = os.getenv('SLACK_TOKEN')
    BASE_DIR = './original/'

    os.makedirs(BASE_DIR, exist_ok=True)

    res = requests.get('https://slack.com/api/emoji.list',
                       headers={'Authorization': f'Bearer {TOKEN}'})
    emojis = res.json()['emoji']

    for alias, emoji_url in emojis.items():
        if (emoji_url.startswith('alias:')):
            continue

        img = download_image(emoji_url)
        if img is None:
            continue

        img_path = make_filename(BASE_DIR, alias, emoji_url)
        save_image(img_path, img)

        sleep(1)


if __name__ == "__main__":
    main()
