from datetime import datetime, timedelta

import aiohttp

from app_parser import *
from my_logger import get_logger


"""
A console utility that returns the EUR and USD rate to PrivatBank over the past few days.
"""


logger = get_logger(__name__)


URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="


def valid_urls(url, count_day):
    now_day = datetime.now()
    new_url = list()
    new_url.append(f"{url + now_day.strftime('%d.%m.%Y')}")

    if count_day > 1:
        for i in range(1, count_day):
            now_day -= timedelta(days=1)
            new_url.append(f"{url + now_day.strftime('%d.%m.%Y')}")

    logger.info(f"{new_url}")


def main(value=days):
    if value > 10 or value < 1:
        result = f"Please enter valid days 1....10"
        logger.info(result)
        print(result)
    else:
        valid_urls(URL, value)


if __name__ == "__main__":
    main()
