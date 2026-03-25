import pandas as pd
from TCs import mechanic_dict

def check_ID(df):
    """
    Function to check ID and month. 

    Only generate T&Cs for promos with unduplicated IDs and within the month / year specified in CLI arguments. 
    """
    # Only check if missing IDs for May onwards (got some mismatched ones from Jan cos silly)
    promo_ID = 1041
    if promo_ID >=1041:
        print("ID checked")
    return 

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
    start_date = "01.02.2026" # pull 
    end_date =  "01.04.2026." # pull 
    mechanic = mechanic_dict.get("Tiered GWP") # pull 
    threshold = "when you spend £65 online" # pull 
            
    return brand, mechanic, threshold, start_date, end_date,


def upload_tc(df):
    """
    Function that takes T&Cs and relevant fields, and populates cells for a single row (Dates / Promo type / T&C etc.)
    """
    # Only upload if promo ID doesn't have corresponding ID in T&Cs tab. 
    print("upload tc empty but works!")
    return
