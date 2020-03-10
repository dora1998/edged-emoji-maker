# edged-emoji-maker

A handy tool edging your Slack emojis with white. It improves emoji visibility when you use Slack in dark mode.

<img src="https://user-images.githubusercontent.com/31735614/72543387-f9930d00-38c8-11ea-8c3e-40d38f812eff.png" width="480px">

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

### Add emojis in bulk (\*)

```
$ find edged -type f | poetry run python add.py
```

### Remove emojis in bulk (\*)

```
$ find edged -type f | awk -F/ '{split($NF, x, "."); print x[1]}' | poetry run python remove.py
```

(\*) These script uses private API. Please run them **at your own risk**.

## FAQ

### Can I use this tool for animated emoji?

~No. If you can, please make a PR to this repo!~

-> Now you can convert animated GIF!

### How can I get private API token?

1. Open emoji admin panel (https://{YOUR_WORKSPACE}.slack.com/customize/emoji).
1. Open Network panel in developer tools.
1. Find XHR request whose request URL begins "https://{YOUR_WORKSPACE}.slack.com/api/emoji.".
1. You can see the token that begins "xoxs-" in "Form Data" panel.

## License

MIT License
