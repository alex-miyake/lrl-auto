import win32com.client as win32
import os
from dotenv import load_dotenv

# get private info 
load_dotenv()
recipients = os.getenv("RECIPIENTS")

def send_report(payload, title):
    """
    Function to take the filled-in report template, and draft it locally in Outlook.
    """
    outlook = win32.Dispatch("Outlook.Application")
    email_draft = outlook.CreateItem(0)
    email_draft.Subject = title
    email_draft.To = recipients
    email_draft.HtmlBody = payload
    email_draft.Save()

    print("Draft saved successfully")
    return 