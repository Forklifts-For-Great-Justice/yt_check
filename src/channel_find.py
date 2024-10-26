from util import channel_check

import argparse


def main(target: str):
    html_text = channel_check.get_page(target)
    channel_id = channel_check.find_channel_id(html_text)
    print(f"located Channel ID: {channel_id}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Takes a youtube url and finds the channel id.")
    parser.add_argument("url", help="youtube url to check")

    args = parser.parse_args()
    main(args.url)
