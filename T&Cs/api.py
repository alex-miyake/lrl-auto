"""
Functions to access NPD file on sharepoint. 
"""
import openpyxl
from openpyxl import Workbook
import pandas as pd
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 
import os

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
    file_path = os.getenv('filename')
    #file_path = r"C:\Users\"
    #df = pd.read_excel(file_path)
    df = "test for now"

    # Need to sort out worksheets

    
    print("connects to real NPD file successfully")
    return df

def test_open():
    """
    Function to open local test excel file, will use for now to get main script working. 

    Parameters:
    -----------

    Returns: 
    --------

    """
    file_path = os.getenv('filename')
    test_path = file_path
    
    # using pandas
    tracker_df = pd.read_excel(test_path, sheet_name=1, skiprows=3, header=0)
    tc_df = pd.read_excel(test_path, sheet_name=2)
    #tracker_df.info()
    #tc_df.info()
    print(tracker_df.head(2), tc_df.head(2))

    print("test file opened successfully")
    return tracker_df, tc_df