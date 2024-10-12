import dotenv
import asyncio
import aiohttp
import discord
import os
import sys
import logging

from yt_check import util


async def main():
    """Load configs"""
    logger = logging.getLogger()
    logger.info("loading .env file")
    dotenv.load_dotenv()
    webhook_url = os.environ["WEBHOOK_URL"]
    developer_key = os.environ["DEVELOPER_KEY"]
    try:
        logger.info("getting all videos")
        videos = util.get_all_videos(developer_key)
        logger.info("building message")
        msg = util.build_message(videos)

        # send message
        async with aiohttp.ClientSession() as session:
            hook = discord.Webhook.from_url(webhook_url, session=session)
            logger.info("sending initial notification")
            await hook.send(util.get_notification())
            logger.info("sending main message")
            await hook.send(msg)

    except util.NoVideosAtAllError as e:
        logging.error(e)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
