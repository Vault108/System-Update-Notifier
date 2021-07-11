import sys
import ubelt
from datetime import date
from dhooks import Webhook, File
from io import BytesIO
from loguru import logger


@logger.catch
def distxt():
    today = date.today().strftime("%F")
    URL = ""
    aptlist = ubelt.cmd("apt list --upgradeable")["out"]
    out = sys.stdout
    with open(today + ".txt", "w") as f:
        sys.stdout = f
        print(aptlist)
        sys.stdout = out
    hook = Webhook(URL)
    file = File(today + ".txt")
    hook.send(file=file)


logger.add("distxt{time}.log")
distxt()
