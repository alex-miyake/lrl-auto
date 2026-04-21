
def decide_colour(number):
    """
    Decide what colour tag the YoY changes will have in html template. 
    """
    number = str(number)
    if '-' in number:
        return "red"
    elif '+' in number:
        return "green"
    else:
        return "black"

def build_report():
    """
    Function to read relevant data, and fill in html template report. 
    """
    # read html template 
    with open("template.html", "r", encoding="utf-8") as f:
        report = f.read()

    # for chat
    values = {
        "{{WEEK}}": "12",
        "{{D2C W SO}}": "5k",
        "{{D2C W YOY}}": "-15",
        "{{SKC W SO}}": "",
        "{{SKC W YOY}}": "+15%",
        "{{SKC W YOY ABS}}": "",
        "{{SKC W FC}}": "",
        "{{SKC YTD SO}}": "",
        "{{SKC YTD YOY}}": "-4%",
        "{{SKC YTD YOY ABS}}": "0k",
        "{{SKC YTD FC}}": "",
        "{{SKC Traffic YOY}}": "",
        "{{SKC CVR YOY}}": "",
        "{{SKC AOV YOY}}": "",
        "{{SKC Comments}}": "comment1 comment 2", 
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

    colours = {}

    # fill in template
    for key, value in values.items():
        # assign colours
        colour_key = key.replace("}}", " COL}}")
        colours[colour_key] = decide_colour(values[key])

        report = report.replace(key, value)
        report = report.replace(colour_key, colours[colour_key])
    
    title = f"D2C W{values['{{WEEK}}']} EPOS Report"

    return report, title