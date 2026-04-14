"""
Functions for actions once file has been accessed / opened.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
import pandas as pd
from TCs import mechanic_dict, brand_dict

def get_data(df, row_no):
    """
    Function that opens NPD file, reads the Promo & GWP Status Tracker tab, and extracts relevant info 

    not using numpy for now, for loop is fine as only doing operations on <100 rows

    NOTES for features:
    - OPTIONAL: include sample name (from LRP samples tracker), if not then just complimentary gift.
    - if has strikethrough then doesnt count! 

    Parameters: 
    -----------

    Returns:
    --------

    """
    # Pull tags. hardcoded row as 1 in main file for now
    brand = df.at[row_no, 'BRAND'] 
    print("TESTING pulled brand as:" + brand)
    start_date = df.at[row_no, 'PLANNED GO LIVE DATE (00:00)']
    end_date = df.at[row_no, 'PLANNED END DATE (00:00)']

    # pull mechanic with regex. 
    mechanic = "Tiered GWP"
    threshold = "when you spend £65 online" # pull 

    print("data pulled successfully")
    return brand, mechanic, threshold, start_date, end_date,


def write_tc(brand, mechanic, threshold, end_date):
    """
    Function that writes longer T&C sections. threshold not always needed. 

    Parameters:
    -----------

    Returns:
    --------
    """
    # build brand dependent strings
    if brand == "LRP":
        website = brand_dict.get("LRP_website")
        valid_site = brand_dict.get("LRP_valid")
        long_ending = brand_dict.get("LRP_long_ending")
    else: 
        website = brand_dict.get("SKC_website")
        valid_site = brand_dict.get("SKC_valid")
        long_ending = brand_dict.get("SKC_long_ending")

    # brand independent strings
    TC_mech = mechanic_dict.get(mechanic)
    end_day = "Until 23.45 on " + end_date 
    short_ending = brand_dict.get("Short_ending") # always same 

    # Short T&C
    long_tc = "str for now"
    print("short T&C:\n" + TC_mech, threshold, website, end_day, valid_site, short_ending)

    # Long T&C
    short_tc = "str for now"
    print("long T&C:\n" + TC_mech, threshold, website, end_day, valid_site + "\n\nT&Cs\n\nClosing date:\n" + end_day + "\n\n" + long_ending)
    return long_tc, short_tc


def upload_tc(row):
    """
    Function that takes T&Cs and relevant fields, and populates cells for a single row (Dates / Promo type / T&C etc.)
    Only upload if promo ID doesn't have corresponding ID in T&Cs tab. 
    CHECK Numpy fastest way to apply changes to df. 
    """
    print("upload tc empty but works!")
    return 


def check_ID(df):
    """
    Function to check ID and month. 
    Only check if missing IDs for May onwards (got some mismatched ones from Jan cos silly)

    Also flag if theres a mismatch, in a new column. 

    use numpy to check the two arrays. 
    EG of numpy for faster operations. 
    conditions = [df['a'] < 3, df['a'] == 3, df['a'] > 3]
    choices = ['low', 'medium', 'high']
    df['category'] = np.select(conditions, choices)

    Only generate T&Cs for promos with unduplicated IDs and within the month / year specified in CLI arguments. 
    also specify at end which IDs had T&Cs written. 
    """
    promo_ID = 1041
    if promo_ID >=1041:
        print("ID checked")
    return 
