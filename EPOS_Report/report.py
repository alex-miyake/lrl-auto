import requests 
import json 

tracker_file = 

def build_report(file):
    report = "msg for now"
    return report

def send_report(msg):
    webhook = ""
    
    payload = {
        "message": msg
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook,headers=headers,data=json.dumps(payload))
    print("request posted successfully")




if __name__=="__main__":
    print("script still works")
    build_report(tracker)
    #send_report(msg)