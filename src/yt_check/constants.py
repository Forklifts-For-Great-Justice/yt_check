""" Constants used by yt_check"""

from enum import StrEnum


class Channels(StrEnum):
    """Channels monitored by yt_check"""

    DRAGONFORCE = "UCIUA7-MNA9NyrpimQo7Dw8g"
    SKELETOR = "UCOYYn-7CTVA1jFtmYOLr8Qw"
    BABYMETAL = "UC33_tIj4m1_XaqfFcomShvw"
    SABATON = "UCjQhd1APsd5NQhiVZV7GYzg"


class Notifications(StrEnum):
    """Notifications used by yt_check"""

    ONE = "Fools! New videos have arrived. Watch them, if you dare!"
    TWO = "Behold, mortals! A feast of new videos awaits. Feast your eyes upon them!"
    THREE = "New videos have been unleashed upon the world. Let the chaos begin!"
    FOUR = "You boob! There are new videos to watch. Don't make me say it again!"
    FIVE = "Another day, another batch of videos. Enjoy, if you can."
