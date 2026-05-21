
def decide_colour(number):
    """
    Decide what colour tag the YoY changes will have in html template. Function used in build_report function
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
    # oepn html template 
    with open("template.html", "r", encoding="utf-8") as f:
        report = f.read()

    # find week (index = week number + 2)
    values_dict['{{WEEK}}'] = str(week_no)
    print(values_dict.keys())
    week_no = int(week_no)
    week_row = skc_df.iloc[6]
    matches = week_row[week_row == week_no].index.tolist()
    col = matches[0]
    ytd_col = 57

    # KPI positions
    kpi_map = [
        ('{{D2C W SO}}',        weekly_df,   4,   1),
        ('{{D2C W YOY}}',       weekly_df,   4,   3),
        ('{{SKC W YOY ABS}}',   weekly_df,   13,  4), 
        ('{{LRP W YOY ABS}}',   weekly_df,  12,  4),   
        ('{{SKC YTD YOY ABS}}', weekly_df,  3,  4),
        ('{{LRP YTD YOY ABS}}', weekly_df,  2,  4), 
        
        ('{{SKC W SO}}',        skc_df,   8,   col),   
        ('{{SKC W YOY}}',       skc_df,  10,  col),   
        ('{{SKC W FC}}',        skc_df,   9,  col),   
        ('{{SKC YTD SO}}',      skc_df,   8,  ytd_col),   
        ('{{SKC YTD YOY}}',     skc_df,  10,  ytd_col),   
        ('{{SKC YTD FC}}',      skc_df,   9,  ytd_col),   
        ('{{SKC Traffic YOY}}', skc_df,  14,  col), 
        ('{{SKC CVR YOY}}',     skc_df,  16,  col),  
        ('{{SKC AOV YOY}}',     skc_df,  18,  col),
        ('{{SKC Comments}}',    skc_df,  85,  col),
        ('{{SKC whats on}}',    skc_df,  83,  col),
        # ('{{SKC whats to come}}',     skc_df,  17,  col),

        ('{{LRP W SO}}',        lrp_df,   8,   col),  
        ('{{LRP W YOY}}',       lrp_df,  10,  col),   
        ('{{LRP W FC}}',        lrp_df,   9,  col),   
        ('{{LRP YTD SO}}',      lrp_df,   8,  ytd_col),   
        ('{{LRP YTD YOY}}',     lrp_df,  10,  ytd_col),   
        ('{{LRP YTD FC}}',      lrp_df,   9,  ytd_col),   
        ('{{LRP Traffic YOY}}', lrp_df,  14,  col),   
        ('{{LRP CVR YOY}}',     lrp_df,  16,  col),   
        ('{{LRP AOV YOY}}',     lrp_df,  18,  col),
        ('{{LRP Comments}}',    lrp_df,  85,  col),
        ('{{LRP whats on}}',    lrp_df,  83,  col),
        # ('{{LRP whats to come}}',     lrp_df,  17,  col)
    ] 
    
    # fill in dict
    for key, df, row, col in kpi_map:
        values_dict[key] = str(df.iat[row,col])
    print(values_dict.keys())    
    
    # CLEAN DICT round values, use K / M / +  
    




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