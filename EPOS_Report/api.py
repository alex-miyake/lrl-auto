import pandas as pd
import os
import sys

"""
example .env contents
RECIPIENTS = ""
filename = "C:/Users/alex/OneDrive/Documents/EPOS (SOANA) Alex.xlsx"
WEEK_NO = "26"
"""

def open_tracker():
    file_path = os.getenv('filename')
    print("got .env file path")
    # excel = pd.ExcelFile(file_path)
    # print("Sheets:", excel.sheet_names)
    
    skc_df = pd.read_excel(file_path, sheet_name='SKC Calendar', header=None, usecols="A:BZ",nrows=119)
    lrp_df = pd.read_excel(file_path, sheet_name='LRP Calendar', header=None, usecols="A:BZ",nrows=119)
    weekly_df = pd.read_excel(file_path, sheet_name='Weekly', header=None, usecols="A:I",nrows=5)
    print("opened all 3 tabs")

    # check 
    #print(skc_df.head(7))
    #print(lrp_df.head(7))
    #print(weekly_df.head())
    return lrp_df, skc_df, weekly_df

def check_ytd(lrp, skc, weekly, week_no):
    week_no = int(week_no)
    tables = []
    if weekly.iat[0,1] != week_no:
        tables.append("Weekly")
    elif lrp.iat[1,57] != week_no:
        tables.append("LRP Calendar")
    elif skc.iat[1,57] != week_no:
        tables.append("SKC Calendar")
    if tables:
        tables = ", ".join(tables)
        error = f"BIG ERROR, the YTD counter in {tables} tab(s) does not match the week you entered."
        print(error)
        sys.exit(1)
    
    return 