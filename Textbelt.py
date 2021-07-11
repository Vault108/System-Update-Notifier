import ubelt
import requests
from loguru import logger
import sys


@logger.catch
def suntext():
    ServerName = "test"  # server name
    updates = ubelt.cmd('sudo apt update')['out'].splitlines()[-1]

    resp = requests.post('https://textbelt.com/text', {
        'phone': '',  # Number to Send to
        'message': ServerName + ": " + updates,
        'key': '',  # textbelt Api key
    })
    logger.info(resp.json())


logger.add("textbelt_{time}.log")

suntext()
