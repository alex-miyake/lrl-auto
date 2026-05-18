import pandas as pd
import os

def connect_test():
    file_path = os.getenv('filename')
    print("got .env variable")
    df = pd.read_excel(file_path)
    print("opened file")
    print(df.head())
    return