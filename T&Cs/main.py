from api import test_open, open_file
from excel import check_ID, write_tc, upload_tc, get_data
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print("main script started")
    tracker_df, tc_df = test_open()
    id_list = check_ID(tracker_df, tc_df)
    tags = get_data(tracker_df)
    write_tc(tags)
    upload_tc(tags)
    print("script works end to end")