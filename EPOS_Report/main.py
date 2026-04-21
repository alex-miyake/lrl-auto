from report import build_report
from email import send_report

if __name__=="__main__":
    print("script starting")
    payload, title = build_report()
    send_report(payload, title)
    print("script finished successfully")
    