"""
Functions to access NPD file on sharepoint. 
"""
import openpyxl
from openpyxl import Workbook
import pandas as pd
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 

def open_file():
    """
    Function to access Excel files in Sharepoint. 

    follow article: https://learn.microsoft.com/en-us/answers/questions/5517764/i-am-looking-for-python-approach-to-accessing-data
    or documentation here: https://pypi.org/project/Office365-REST-Python-Client/#Working-with-SharePoint-API
    Parameters:
    -----------

    Returns:
    --------

    """    
    
    # Access sharepoint
    print("connects ok I think")

    # Load into pandas
    df = "pandas df"
    return df

def test_open():
    """
    Function to open local test excel file, will use for now to get main script working. 

    Articles to follow: 
    https://www.geeksforgeeks.org/python/formatting-cells-using-openpyxl-in-python/ 
    https://www.geeksforgeeks.org/python/working-with-excel-spreadsheets-in-python/ 

    Parameters:
    -----------

    Returns: 
    --------

    """
    test_path = "test_NPD_file.xlsx"
    
    # using pandas
    ID_df = pd.read_excel(test_path, sheet_name=0, skiprows=3, header=0)
    tc_df = pd.read_excel(test_path, sheet_name=1)
    ID_df.info()
    tc_df.info()
    print(ID_df.head(2), tc_df.head(2))

    print("test file opened successfully")
    return ID_df, tc_df