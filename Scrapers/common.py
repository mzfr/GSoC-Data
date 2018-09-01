import json
import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache("scraper")


def getPage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    return soup


def dumper(json_data, json_file):
    """Makes json file from the given data"""
    with open(json_file, 'w') as f:
        json.dump(json_data, f)
