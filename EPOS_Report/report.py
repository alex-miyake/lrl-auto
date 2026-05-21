
def decide_colour(n):
    """
    Decide what colour tag the YoY changes will have in html template. Function used in build_report function
    """
    n = str(n)
    if '-' in n:
        return "red"
    elif '+' in n:
        return "green"
    else:
        return "black"

def format_percent(value):
    value = round(float(value) * 100)
    if value > 0:
        evol = f"+{value}%"
    else:
        evol = f"{value}%"
    return evol

def format_SO(value):
    value = float(value)
    if abs(value) >= 1000000:
        rounded = round(value/1000000,2)
        SO = f"£{rounded}M"
    else:
        rounded = round(value/1000)
        SO = f"£{rounded}K"
    return SO

def format_abs(value):
    value = float(value)
    if abs(value) >= 1000000:
        rounded = round(value/1000000,2)
        abs_SO = f"£{rounded}M"
    else:
        rounded = round(value/1000)
        abs_SO = f"£{rounded}K"
    if value>0:
        abs_SO = f"+{abs_SO}"
    return abs_SO

def build_report(values_dict, week_no, lrp_df, skc_df, weekly_df):
    """
    Function to read relevant data, and fill in html template report. 
    """
    # oepn html template 
    with open("template.html", "r", encoding="utf-8") as f:
        report = f.read()

    # find week (index = week number + 2)
    values_dict['{{WEEK}}'] = str(week_no)
    #print(values_dict.keys())
    week_no = int(week_no)
    week_row = skc_df.iloc[6]
    matches = week_row[week_row == week_no].index.tolist()
    col = matches[0]
    ytd_col = 57

    # KPI positions + formatting type (function name)
    kpi_map = [
        ('{{D2C W SO}}',        weekly_df,   4,   1, format_SO),
        ('{{D2C W YOY}}',       weekly_df,   4,   3, format_percent),
        ('{{SKC W YOY ABS}}',   weekly_df,   13,  4, format_abs), 
        ('{{LRP W YOY ABS}}',   weekly_df,  12,  4, format_abs),   
        ('{{SKC YTD YOY ABS}}', weekly_df,  3,  4, format_abs),
        ('{{LRP YTD YOY ABS}}', weekly_df,  2,  4, format_abs), 
        
        ('{{SKC W SO}}',        skc_df,   8,   col, format_SO),   
        ('{{SKC W YOY}}',       skc_df,  10,  col, format_percent),   
        ('{{SKC W FC}}',        skc_df,   9,  col, format_percent),   
        ('{{SKC YTD SO}}',      skc_df,   8,  ytd_col, format_SO),   
        ('{{SKC YTD YOY}}',     skc_df,  10,  ytd_col, format_percent),   
        ('{{SKC YTD FC}}',      skc_df,   9,  ytd_col, format_percent),   
        ('{{SKC Traffic YOY}}', skc_df,  14,  col, format_percent), 
        ('{{SKC CVR YOY}}',     skc_df,  16,  col, format_percent),  
        ('{{SKC AOV YOY}}',     skc_df,  18,  col, format_percent),
        ('{{SKC Comments}}',    skc_df,  85,  col, str),
        ('{{SKC whats on}}',    skc_df,  83,  col, str),
        # ('{{SKC whats to come}}',     skc_df,  17,  col),

        ('{{LRP W SO}}',        lrp_df,   8,   col, format_SO),  
        ('{{LRP W YOY}}',       lrp_df,  10,  col, format_percent),   
        ('{{LRP W FC}}',        lrp_df,   9,  col, format_percent),   
        ('{{LRP YTD SO}}',      lrp_df,   8,  ytd_col, format_SO),   
        ('{{LRP YTD YOY}}',     lrp_df,  10,  ytd_col, format_percent),   
        ('{{LRP YTD FC}}',      lrp_df,   9,  ytd_col, format_percent),   
        ('{{LRP Traffic YOY}}', lrp_df,  14,  col, format_percent),   
        ('{{LRP CVR YOY}}',     lrp_df,  16,  col, format_percent),   
        ('{{LRP AOV YOY}}',     lrp_df,  18,  col, format_percent),
        ('{{LRP Comments}}',    lrp_df,  85,  col, str),
        ('{{LRP whats on}}',    lrp_df,  83,  col, str),
        # ('{{LRP whats to come}}',     lrp_df,  17,  col)
    ] 
    
    # fill in / clean dict (type calls the function name)
    for key, df, row, col, type in kpi_map:
        values_dict[key] = type(str(df.iat[row,col]))
    #print(values_dict.keys())
     
    # Assign colour
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