
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

def build_report(values_dict, week_no, lrp_df, skc_df, weekly_df):
    """
    Function to read relevant data, and fill in html template report. 
    """
    # read html template 
    with open("template.html", "r", encoding="utf-8") as f:
        report = f.read()

    # fill in dict
    
    # set up rows to KPI
    # find week (same for both)
    week_no = int(week_no)
    week_column = skc_df.iloc[6]
    # for row in week:
        # fill in dict

    # round values, use K / M etc. 





    # 
    colours = {}
    
    for key, value in values_dict.items():
        # setup colour dict
        colour_key = key.replace("}}", " COL}}")
        colours[colour_key] = decide_colour(values_dict[key])

        # fill html template
        report = report.replace(key, value)
        report = report.replace(colour_key, colours[colour_key])
    
    title = f"D2C W{values_dict['{{WEEK}}']} EPOS Report"

    return report, title