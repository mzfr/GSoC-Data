import json
import aiohttp
from bs4 import BeautifulSoup


async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = await response.read()

    return BeautifulSoup(soup.decode('utf-8'), "lxml")


def dumper(json_data, json_file):
    """Makes json file from the given data"""
    with open(json_file, 'w') as f:
        json.dump(json_data, f)
