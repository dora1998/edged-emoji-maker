# edged-emoji-maker

A handy tool edging your Slack emojis with white. It improves emoji visibility when you use Slack in dark mode.

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

(This script is in development. Sorry...)

## License

MIT License
