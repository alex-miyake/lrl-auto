from api import test_open
from excel import check_ID, write_tc, upload_tc, get_data

if __name__ == "__main__":
    print("main script started")
    tracker_df, tc_df = test_open()
    #check_ID(df)
    tags = get_data(tracker_df)
    write_tc(tags)
    upload_tc(tags)
    print("script works end to end")