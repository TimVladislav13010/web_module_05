from datetime import datetime, timedelta

import aiohttp
import asyncio
import platform

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

    return new_url


async def request(url, session):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                r = await response.json()
                return r
            logger.error(f"Error status {response.status} for {url}")
    except aiohttp.ClientConnectorError as e:
        logger.error(f"Connection error {url}: {e}")
    return None


async def main(value=days):
    if value > 10 or value < 1:
        result = f"Please enter valid days 1....10"
        logger.info(result)
    else:
        urls = valid_urls(URL, value)
        async with aiohttp.ClientSession() as session:
            list_function = [request(url, session) for url in urls]
            result = await asyncio.gather(*list_function)
            return result


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    results = asyncio.run(main())
    print(results)
