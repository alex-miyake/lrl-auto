"""
Functions for actions once file has been accessed / opened.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
import pandas as pd
from dict import mechanic_dict, brand_dict
import os

def assign_mechanic(row):
    """
    Decides promo mechanic type for dict for a single row, using regex
    """

    
    return mechanic, threshold

def get_data(df):
    """
    Function that opens NPD file, reads the Promo & GWP Status Tracker tab, and extracts relevant info 

    NOTES for features: 
    - OPTIONAL: include sample name (from LRP samples tracker), if not then just complimentary gift.
    - if has strikethrough then doesnt count! 

    Parameters: 
    -----------

    Returns:
    --------

    """
    # Hardcoded for a single row rn
    row_no = 0

    # Pull tags 
    ID = df.at[row_no, 'UNIQUE ID']
    brand = df.at[row_no, 'BRAND']
    month = df.at[row_no, 'MONTH']
    description = df.at[row_no, 'MECHANIC']
    print("TESTING pulled brand as:" + brand)
    start_date = df.at[row_no, 'PLANNED GO LIVE DATE (00:00)']
    end_date = df.at[row_no, 'PLANNED END  DATE (00:00)']
    promo_type = df.at[row_no, 'PROMOTION TYPE']

    mechanic, threshold = df.apply(assign_mechanic, axis=1)
    # NEED if threshold empty then no impact on sentence

    # all tags in a dict, for next functions 
    tags = {
        "ID": ID,
        "month": month,
        "brand": brand,
        "description": description,
        "mechanic": mechanic,
        "threshold": threshold,
        "start_date": start_date,
        "end_date": end_date,
    }    

    print("data pulled successfully")
    return tags

def write_tc(tags):
    """
    Function that writes longer T&C sections. threshold not always needed. 

    Parameters:
    -----------

    Returns:
    --------
    """
    # extract tags
    brand = tags.get("brand")
    mechanic = tags.get("mechanic")
    threshold = tags.get("threshold")
    end_date = tags.get("end_date")

    # clean tag
    end_date = end_date.strftime("%Y-%m-%d")

    # brand dependent stuff
    if brand == "LRP":
        website = brand_dict.get("LRP_website")
        valid_site = brand_dict.get("LRP_valid")
        long_ending = brand_dict.get("LRP_long_ending")
    else: 
        website = brand_dict.get("SKC_website")
        valid_site = brand_dict.get("SKC_valid")
        long_ending = brand_dict.get("SKC_long_ending")

    # universal stuff
    TC_mech = mechanic_dict.get(mechanic)
    end_day = "Until 23.45 on " + end_date 
    short_ending = brand_dict.get("Short_ending") 

    # Write T&Cs
    short_tc = (f"{TC_mech} {threshold} {website} {end_day} {valid_site} {short_ending}")
    long_tc = (
        f"{TC_mech} {threshold} {website} {end_day} {valid_site}"
        f"\n\nT&Cs\n\nClosing date:\n{end_day}\n\n{long_ending}")

    print("T&Cs successfully written")

    # add new entries to tags dict
    tags['long tc'] = long_tc
    tags['short tc'] = short_tc

    return tags

def upload_tc(tags):
    """
    Function that takes T&Cs and relevant fields, and populates cells for a single row (Dates / Promo type / T&C etc.)
    Only upload if promo ID doesn't have corresponding ID in T&Cs tab. 
    CHECK Numpy fastest way to apply changes to df. 
    """
    # extract relevant tags
    ID = tags.get("ID")
    month = tags.get("month")
    brand = tags.get("brand")
    description = tags.get("description")
    start_date = tags.get("start_date")
    end_date = tags.get("end_date")
    long_tc = tags.get("long tc")
    short_tc = tags.get("short tc")

    # clean tags
    end_date = end_date.strftime("%Y-%m-%d")
    start_date = start_date.strftime("%Y-%m-%d")

    # my_df = pd.DataFrame(columns=["ID", "Month", "Brand", "start_date", "end_date", "Short T&Cs", "Long T&Cs"])
    

    # populate 1 row into new df (inefficient for now)
    rows = []
    rows.append({
        "ID"        : ID,
        "Month"     : month,
        "Brand"     : brand,
        "Mechanic"  : description,
        "start_date": start_date,
        "end_date"  : end_date, 
        "Short T&Cs": short_tc, 
        "Long T&Cs" : long_tc
    })
    my_df = pd.DataFrame(rows)
    print(my_df.head(2))

    # Excel writer
    file_path = os.getenv('filename')
    writer = pd.ExcelWriter(
        path= file_path,
        engine='openpyxl',
        mode='a',                   
        if_sheet_exists='overlay'
    )
    TC_TAB = os.getenv('TC_TAB')
    my_df.to_excel(
        writer,
        sheet_name= TC_TAB,     # USE .env file later
        columns=["ID", "Month", "Brand", "Mechanic", "start_date", "end_date", "Short T&Cs", "Long T&Cs"],
        header=False,
        index=False,
        startrow=3,          # need dynamic later  
        startcol=0
    )
    # save changes
    writer.close()
    print("file successfully populated")

    return 

def check_ID(tracker_df, tc_df):
    """
    Function to check ID and month. 
    Only check if missing IDs from Jan onwards. Flag if theres a mismatch, in a new column. 

    Only generate T&Cs for promos with unduplicated IDs and within the month / year specified in CLI arguments. 
    also specify at end which IDs had T&Cs written. 
    """
    # hard coded for now
    MONTH = os.getenv('MONTH')
    
    tracker_set = set(tracker_df['UNIQUE ID'])
    tc_set = set(tc_df['UNIQUE PROMO ID'])

    matches = tracker_set & tc_set
    id_list = tracker_set - tc_set
    error_list = tc_set - tracker_set

    print("ID successfully checked:")
    print(id_list)
    print("mis-created IDs:")
    print(error_list)
    return id_list
