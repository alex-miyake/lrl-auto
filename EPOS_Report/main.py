from report import build_report
from email import send_report

if __name__=="__main__":
    print("script starting")
    tracker = "placeholder_file.xlsx"
    payload = build_report(tracker)
    send_report(payload)