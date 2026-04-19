import pandas as pd

FILEPATH = "https://loreal-my.sharepoint.com/personal/alex_miyake_loreal_com/Documents/Documents/EPOS%20PBI%20Alex%20.xlsx?web=1"

def build_report(file):
    """
    Function to load EPOS tracker, read relevant data, and fill in EPOS report template. 
    """
    # load in html template 
    with open("template.html", "r", encoding="utf-8") as f:
        report = f.read()

    # read values from EPOS tracker
    df = pd.read_excel(FILEPATH, sheet_name="SKC Calendar")
    print("opened EPOS tracker successfully")

    # allocate values 
    values = {
        "{{WEEK}}": "",
        "{{D2C W SO}}": "",
        "{{D2C W YOY}}": "",
        "{{SKC W SO}}": "",
        "{{SKC W YOY}}": "",
        "{{SKC W YOY ABS}}": "",
        "{{SKC W FC}}": "",
        "{{SKC YTD SO}}": "",
        "{{SKC YTD YOY}}": "",
        "{{SKC YTD YOY ABS}}": "",
        "{{SKC YTD FC}}": "",
        "{{SKC Traffic YOY}}": "",
        "{{SKC CVR YOY}}": "",
        "{{SKC AOV YOY}}": "",
        "{{SKC Comments}}": "", 
        "{{SKC whats on}}": "Country & TownHouse Competition and welcome GWP, Sitewide Tiered GWP", # Hardcoded
        "{{SKC whats to come}}": "", # Hardcoded
        "{{LRP W SO}}": "",
        "{{LRP W YOY}}": "",
        "{{LRP W YOY ABS}}": "",
        "{{LRP W FC}}": "",
        "{{LRP YTD SO}}": "",
        "{{LRP YTD YOY}}": "",
        "{{LRP YTD YOY ABS}}": "",
        "{{LRP YTD FC}}": "",
        "{{LRP Traffic YOY}}": "",
        "{{LRP CVR YOY}}": "",
        "{{LRP AOV YOY}}": "",
        "{{LRP Comments}}": "",
        "{{LRP whats on}}": "Sitewide Tiered GWP", # Hardcoded
        "{{LRP whats to come}}": "", # Hardcoded
    }

    # fill in template 
    for placeholder, value in values.items():
        report = report.replace(placeholder, value)

    return report 