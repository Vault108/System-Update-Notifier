import sys
import ubelt
from datetime import date
from dhooks import Webhook, File
from fpdf import FPDF
from io import BytesIO
from loguru import logger
from ratelimit import limits


@logger.catch
@limits(calls=1, period=120) # limits to 1 call per 120 seconds. 
def dispdf():
    today = date.today().strftime("%F")
    URL = ""
    aptlist = ubelt.cmd("apt list --upgradeable")["out"]
    out = sys.stdout
    with open(today + ".txt", "w") as f:
        sys.stdout = f
        print(aptlist)
        sys.stdout = out
    pdf = FPDF("P", "mm", (297, 210))
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    a = open(today + ".txt", "r")
    for x in a:
        pdf.cell(200, 7, txt=x, ln=1)
    pdf.output(today + ".pdf")
    hook = Webhook(URL)
    file = File(today + ".pdf")
    hook.send(file=file)


logger.add("dispdf{time}.log")
dispdf()
