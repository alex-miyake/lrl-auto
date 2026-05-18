from report import build_report
from email import send_report
from api import connect_test
from dotenv import load_dotenv

if __name__=="__main__":
    print("script starting")
    load_dotenv()
    connect_test()
    
    # payload, title = build_report()
    # send_report(payload, title)
    print("script finished successfully")
    