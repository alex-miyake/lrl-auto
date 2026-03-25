"""
Dictionary with set phrases based on data parsed from NPD File. 
Function that writes T&Cs 

(Writing T&Cs is very formulaic, this selection should be fine for now)
"""

mechanic_dict = {
    "GWP": "",
    "% OFF": "",
    "Both" : "",
    "Tiered GWP": "*Receive a complimentary gift" 
    }

brand_dict = {
    "Short_ending" : " Incomplete, illegal, misdirected or late redemptions will not be valid. Promoter is not responsible for redemptions lost, damaged or delayed due to technical or connectivity or other problems. Subject to availability, whilst stocks last.",
    
    "LRP_website" : "at www.laroche-posay.co.uk.",
    "SKC_website" : "at www.skinceuticals.co.uk.",
    
    "LRP_valid" : "Valid online at www.laroche-posay.co.uk.",
    "SKC_valid" : "Valid online at www.skinceuticals.co.uk.", 
    
    "LRP_long_ending" : "Conditions of offer:\n\n18+ only, one transaction per customer, UK only. This promotion is not available in conjunction with any other offers. Subject to availability, whilst stocks last.\n\nOnline qualifications:\nOffer available at laroche-posay.co.uk Incomplete, illegal, misdirected or late redemptions will not be valid. Promoter is not responsible for redemptions lost, damaged or delayed due to technical or connectivity or other problems. Promoter: La Roche-Posay, a trading division of L’Oréal (U.K.) Limited, Gateway Central White City Place 187 Wood Lane, London W12 7SA.",
    "SKC_long_ending" : "Conditions of offer:\n\n18+ only, one transaction per customer, UK only. This promotion is not available in conjunction with any other offers. Subject to availability, whilst stocks last.\n\nOnline qualifications:\nOffer available at skinceuticals.co.uk Incomplete, illegal, misdirected or late redemptions will not be valid. Promoter is not responsible for redemptions lost, damaged or delayed due to technical or connectivity or other problems. Promoter: SkinCeuticals, a trading division of L’Oréal (U.K.) Limited, Gateway Central White City Place 187 Wood Lane, London W12 7SA."
    }


def write_tc(brand, mechanic, threshold, end_date):
    """
    Function that writes longer T&C sections. 

    Parameters:
    -----------

    Returns:
    --------
    """
    if brand == "LRP":
        website = brand_dict.get("LRP_website")
        valid_site = brand_dict.get("LRP_valid")
        long_ending = brand_dict.get("LRP_long_ending")
    else: 
        website = brand_dict.get("SKC_website")
        valid_site = brand_dict.get("SKC_valid")
        long_ending = brand_dict.get("SKC_long_ending")

    end_day = "Until 23.45 on " + end_date # might not work
    short_ending = brand_dict.get("Short_ending") # always same 

    # Short T&C
    long_tc = "str for now"
    print("short T&C:\n" + mechanic, threshold, website, end_day, valid_site, short_ending)

    # Long T&C
    short_tc = "str for now"
    print("long T&C:\n" + mechanic, threshold, website, end_day, valid_site + "\n\nT&Cs\n\nClosing date:\n" + end_day + "\n\n" + long_ending)
    return long_tc, short_tc