# Listen To This BOT

A bot that gets music posted in [r/listentothis](https://www.reddit.com/r/listentothis/) and upload these in many playlists by genre on YouTube.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the bot and how to install them

```
Python 3 (up to 3.6)
```

The `pip` package management tool

PRAW. It is a python package that allows for simple access to reddit’s API. See docs [here](https://praw.readthedocs.io/en/v3.1.0/index.html)

```
pip install praw
```

Get the `client_id` and `client_secret` [here](https://github.com/reddit-archive/reddit/wiki/OAuth2)

The Google APIs Client Library for Python:

```
pip install --upgrade google-api-python-client
```

The google-auth-oauthlib and google-auth-httplib2 libraries for user authorization.

```
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```

Get the OAuth 2.0 doing this [this](https://developers.google.com/identity/protocols/oauth2/native-app#prerequisites)

Then, go to [here](https://console.developers.google.com/), clik on Credentials and download the client_secret.json in OAuth 2.0 ID Client section.

### Installing

You only have to run the main.py file:

```
python3 main.py
```

## Built With

- [API Reddit](https://www.reddit.com/dev/api/) - The web we get the music.
- [PRAW](https://praw.readthedocs.io/en/v3.1.0/index.html) A Python Reddit API Wrapper.
- [API YouTube v3](https://developers.google.com/youtube/v3/getting-started) - Used to upload the playlist.

## Demo

A simple test with only a playlist.

![](bot-reddit.gif)

## Authors

- **Nicolás Liendro** - _Initial work_ - [GitLab](https://gitlab.com/NicoLiendro14),
  [GitHub](https://github.com/NicoLiendro14) and
  [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-liendro-00248a178/)
