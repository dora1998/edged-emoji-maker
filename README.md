# edged-emoji-maker

A handy tool edging your Slack emojis with white. It improves emoji visibility when you use Slack in dark mode.

<img src="https://user-images.githubusercontent.com/31735614/72543387-f9930d00-38c8-11ea-8c3e-40d38f812eff.png" style="max-width: 480px;">

## Setup

```
$ poetry install
$ cp .env.sample .env
```

If you want to import emojis from your workspace, get OAuth Token [here](https://api.slack.com/apps?new_app=1). Then set the token in .env file.

### Requirements

- Python 3.7 or higher
- Poetry

## Basic Usage

### Import emojis from a workspace

```
$ poetry run python import.py
```

### Edge emojis

```
$ poetry run python convert.py
```

## FAQ

### Can I use this tool for animated emoji?

No. If you can, please make a PR to this repo!

### How do I add edged emojis in a lump?

Install the Chrome extension "Neutral Face Emoji Tools" [here](https://chrome.google.com/webstore/detail/neutral-face-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej).

## License

MIT License
