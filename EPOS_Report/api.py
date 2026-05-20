import pandas as pd
import os

def open_tracker():
    file_path = os.getenv('filename')
    print("got .env file path")
    # excel = pd.ExcelFile(file_path)
    # print("Sheets:", excel.sheet_names)
        
    skc_df = pd.read_excel(file_path, sheet_name='SKC Calendar', header=None, usecols="A:BZ",nrows=119)
    lrp_df = pd.read_excel(file_path, sheet_name='LRP Calendar', header=None, usecols="A:BZ",nrows=119)
    weekly_df = pd.read_excel(file_path, sheet_name='Weekly', header=None, usecols="A:E",nrows=4)
    print("opened all 3 files")

    # check
    print(skc_df.head(10))
    print(lrp_df.head(10))
    print(weekly_df.head())
    return lrp_df, skc_df, weekly_df