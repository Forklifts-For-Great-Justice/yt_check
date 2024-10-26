import requests
import re


class NoChannelIDError(Exception):
    """Raised when text did not have a channel id."""


def get_page(url: str) -> str:
    return requests.get(url).text


def find_channel_id(html: str) -> str:
    data = re.search(r'content="https://www.youtube.com/channel/(.+?)">', html)
    if data is None:
        raise NoChannelIDError("Could not find channel")
    return data.group(1)
