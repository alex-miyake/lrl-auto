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

def test_open(excel_file):
    """
    Function to open local test excel file, will use for now to get main script working. 

    Parameters:
    -----------

    Returns:
    --------

    """


    print("opened file successfully")