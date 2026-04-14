import win32com.client as win32

recipients = "marco.fang@loreal.com"

def send_report(payload):
    outlook = win32.Dispatch("Outlook.Application")
    email_draft = outlook.CreateItem(0)
    email_draft.Subject = "DRAFT: D2C W13 EPOS Report"
    email_draft.To = recipients
    email_draft.HtmlBody = payload
    email_draft.Save()

    print("Draft saved successfully")
    return 