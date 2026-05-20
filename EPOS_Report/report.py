
def decide_colour(number):
    """
    Decide what colour tag the YoY changes will have in html template. 
    Function used in build_report function
    """
    number = str(number)
    if '-' in number:
        return "red"
    elif '+' in number:
        return "green"
    else:
        return "black"

def build_report(values_dict, week_no, kpi_map, lrp_df, skc_df, weekly_df):
    """
    Function to read relevant data, and fill in html template report. 
    """
    # read html template 
    with open("template.html", "r", encoding="utf-8") as f:
        report = f.read()

    week_no = int(week_no)
    week_row = skc_df.iloc[6]
    matches = week_row[week_row == week_no].index.tolist()
    # column index will be week number + 2
    col = matches[0]
    
    # fill in for each brand 
    for key, df, row, col in kpi_map:
        values_dict = {key: str(df.iat[row,col])}
    #values_dict['{{SKC W SO}}'] = str(skc_df.iat[8, col])
    
    # CLEAN DICT round values, use K / M etc. 





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