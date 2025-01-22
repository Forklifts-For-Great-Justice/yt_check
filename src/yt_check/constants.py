""" Constants used by yt_check"""

from enum import StrEnum


class Channels(StrEnum):
    """Channels monitored by yt_check"""

    DRAGONFORCE = "UCIUA7-MNA9NyrpimQo7Dw8g"
    SKELETOR = "UCOYYn-7CTVA1jFtmYOLr8Qw"
    BABYMETAL = "UC33_tIj4m1_XaqfFcomShvw"
    SABATON = "UCjQhd1APsd5NQhiVZV7GYzg"
    NEKROGOBLIKON = "UCIlCG-eRqxjgtbbp9AzeNeg"
    BLODDYWOOD = "UChDkP71cJOHop-iRgl_8pVg"
    NAPLAM_RECORDS = "UCG7AaCh_CiG6pq_rRDNw72A"
    SORA_THE_TROLL = "UCMj4YareOFuEfxUBbncWF9w"
    FORKLIFT_JOE = "UC-sOORmpV5BH3HUqZ3I9Cxg"
    BLUTENGEL = "UCySqfRjNa9FjZ7lvuTRa5UQ"


class Notifications(StrEnum):
    """Notifications used by yt_check"""

    ONE = "Fools! New videos have arrived. Watch them, if you dare!"
    TWO = "Behold, mortals! A feast of new videos awaits. Feast your eyes upon them!"
    THREE = "New videos have been unleashed upon the world. Let the chaos begin!"
    FOUR = "You boob! There are new videos to watch. Don't make me say it again!"
    FIVE = "Another day, another batch of videos. Enjoy, if you can."
    SIX = (
        "By the power of Evil-Lyn, new videos have arrived! Prepare to cringe, He-Man!"
    )
    SEVEN = "Hordak! I sense... new videos! They will be devoured by my insatiable hunger for... views!"
    EIGHT = "Fools! New videos have been unleashed upon this pitiful channel! Witness their... glorious mediocrity!"
    NINE = "You Boob! New videos have been uploaded. Feast your eyes on this digital garbage!"
    TEN = "This channel is now contaminated... with new videos! Despair, He-Man!"
