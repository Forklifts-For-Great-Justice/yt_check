import google_auth_oauthlib.flow
import googleapiclient.discovery
import datetime
import random
from typing import Dict
from typing import List
from typing import Iterable

from . import constants


class NoVideosError(Exception):
    """The specified channel has no videos."""


class NoVideosAtAllError(Exception):
    """No channels have videos."""


def parse_videos(video_list: Iterable, max_video_age: int = 24) -> List[str]:
    videos = []
    for video in video_list:
        video_id = video["id"].get("videoId", None)
        if video_id is None:
            continue
        current = {
            "url": f"https://youtube.com/watch?v={video['id']['videoId']}",
            "title": video["snippet"]["title"],
            "description": video["snippet"]["description"],
            "publishedAt": datetime.datetime.fromisoformat(
                video["snippet"]["publishedAt"]
            ),
        }
        if current["publishedAt"] > datetime.datetime.now(
            datetime.timezone.utc
        ) - datetime.timedelta(hours=max_video_age):
            videos.append(current)

    return videos


def get_latest_videos(channel_id: constants.Channels, developer_key: str) -> List[Dict]:
    """Fetches the latest videos from a specified YouTube channel.

    Args:
        channel_id (Channels): The ID of the YouTube channel.
        developer_key (str): The developer key to use.

    Returns:
        list: A list of dictionaries containing video information.
    """

    # Replace 'YOUR_API_KEY' with your actual API key
    api_service_name = "youtube"
    api_version = "v3"
    client = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key
    )

    request = client.search().list(
        part="id,snippet", channelId=channel_id, order="date", maxResults=10
    )

    response = request.execute()

    videos = parse_videos(response["items"], 24)

    if not videos:
        raise NoVideosError("No videos for channel: {}".format(channel_id))
    return videos


def get_notification() -> str:
    """Returns a random notification message.

    Returns:
        randomly selected notification message.
    """
    notifications = []
    for notification in constants.Notifications:
        notifications.append(notification)

    return f"# {random.choice(notifications)}"


def build_message(channel_videos: Iterable) -> str:
    msg = ""
    for videos in channel_videos:
        for video in videos:
            msg += f"## {video['title']}\n{video['description']}\n{video['url']}\n"

    return msg


def get_all_videos(developer_key: str) -> str:
    videos = []
    for channel_id in constants.Channels:
        try:
            videos.append(get_latest_videos(channel_id, developer_key))
        except NoVideosError:
            pass

    if not videos:
        raise NoVideosAtAllError("Seriously, there's no videos at all.")
    return videos
