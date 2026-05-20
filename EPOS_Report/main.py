from report import build_report
from email import send_report
from api import open_tracker
from dict import values, kpi_map
from dotenv import load_dotenv
import os

if __name__=="__main__":
    print("script starting")
    load_dotenv()
    week = os.getenv('WEEK_NO')
    lrp, skc, weekly = open_tracker()
    payload, title = build_report(values, week, kpi_map, lrp, skc, weekly)
    send_report(payload, title)
    print("script finished successfully")
    