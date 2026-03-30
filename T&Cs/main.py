from api import test_open
from excel import check_ID, write_tc, upload_tc, get_data

if __name__ == "__main__":
    print("main script working")
    ID_df, tc_df = test_open()
    #check_ID(df)
    signature, mech, thresh, start_date, end_date = get_data(ID_df)
    #write_tc(signature, mech, thresh, end_date) 
    #upload_tc(df) 
    print("works end to end")