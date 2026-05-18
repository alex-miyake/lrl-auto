import pandas as pd

def connect_test():
    file_path = r"C:\Users\alex.miyake\OneDrive - L'Oréal\Documents\EPOS PBI Alex .xlsx"
    df = pd.read_excel(file_path)
    print(df.head())
    return