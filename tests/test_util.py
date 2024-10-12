from freezegun import freeze_time
import unittest
import datetime

from yt_check import util
from yt_check import constants


class UtilTest(unittest.TestCase):

    def test_notification(self):
        notification = util.get_notification()
        self.assertTrue(notification.startswith("# "))
        self.assertTrue(notification[2:] in constants.Notifications)
        self.assertIsInstance(notification, str)

    @freeze_time("2024-10-02")
    def test_parse_video(self):
        videos = [
            {
                "id": {"videoId": "test_id"},
                "snippet": {
                    "title": "video_name",
                    "description": "its a video",
                    "publishedAt": "2024-10-03T22:58:42Z",
                },
            }
        ]
        actual = util.parse_videos(videos)
        want = [
            {
                "url": "https://youtube.com/watch?v=test_id",
                "title": "video_name",
                "description": "its a video",
                "publishedAt": datetime.datetime.fromisoformat("2024-10-03T22:58:42Z"),
            }
        ]
        self.assertListEqual(actual, want)

    def test_build_message(self):
        videos = [
            [
                {
                    "title": "video_name",
                    "description": "its a video",
                    "url": "https://youtube.com/watch?v=test_id",
                }
            ]
        ]
        actual = util.build_message(videos)
        want = "## video_name\nits a video\nhttps://youtube.com/watch?v=test_id\n"
        self.assertEqual(actual, want)
