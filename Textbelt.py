import ubelt
import requests
from loguru import logger
import sys
from ratelimits import limits


@logger.catch
@limits(calls=1, period=120)  # 1 call per 120 seconds.
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
