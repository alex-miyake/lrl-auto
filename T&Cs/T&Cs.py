import pandas as pd
from dict import mechanic_dict, brand_dict
from api import test_open

print("hello working")

def check_ID():
    """
    Function to check ID and month. 

    Only generate T&Cs for promos with unduplicated IDs and within the month / year specified in CLI arguments. 
    """

def get_data(df):
    """
    Function that opens NPD file, reads the Promo & GWP Status Tracker tab, and extracts relevant info 

    Parameters: 
    -----------

    Returns:
    --------

    """
    # Mechanic: include sample name (from LRP samples tracker), if not then just complimentary gift.
    # if has strikethrough then doesnt count! 
    # Open file, bullet proof if tab name changes 


    # Data just to fill 


    # Data needed to write
    brand = "LRP" # pull 
    end_date =  "Until 23.45 on 01.04.2026." # pull 
    mechanic = mechanic_dict.get("Tiered GWP") # pull 
    threshold = "when you spend £65 online" # pull 
    
    if brand == "LRP":
        website = brand_dict.get("LRP_website")
        valid_site = brand_dict.get("LRP_valid")
        long_ending = brand_dict.get("LRP_long_ending")
    else: 
        website = brand_dict.get("SKC_website")
        valid_site = brand_dict.get("SKC_valid")
        long_ending = brand_dict.get("SKC_long_ending")

    short_ending = brand_dict.get("Short_ending") # always same 
        
    return mechanic, threshold, website, end_date, valid_site, short_ending, long_ending


def write_tc(mechanic, threshold, website, end_day, legal_site, s_ending, l_ending):
    """
    Function that writes longer T&C sections. 

    Parameters:
    -----------

    Returns:
    --------
    """
    # Short T&C
    print("short T&C:\n" + mechanic, threshold, website, end_day, legal_site, s_ending)

    # Long T&C
    print("long T&C:\n" + mechanic, threshold, website, end_day, legal_site + "\n\nT&Cs\n\nClosing date:\n" + end_day + "\n\n" + l_ending)
    return 


def upload_tc():
    """
    Function that takes T&Cs and relevant fields, and populates cells for a single row (Dates / Promo type / T&C etc.)
    """
    # Only upload if promo ID doesn't have corresponding ID in T&Cs tab. 
    return



if __name__ == "__main__":
    df = test_open()
    # check ID
    # mech, thresh, wsite, e_d, v_site, s_end, l_end = get_data()
    # write_tc(mech, thresh, wsite, e_d, v_site, s_end, l_end)
    upload_tc()