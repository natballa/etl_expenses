import argparse
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    parser = argparse.ArgumentParser(description="Run full ETL pipeline")
    parser.add_argument("--since", type=str, help="Filter data from this date (YYYY-MM-DD)")
    parser.add_argument("--load", action="store_true", help="Save transformed data to database")
    args = parser.parse_args()

    # 1️⃣ Extract
    df = extract_data(since=args.since)

    # 2️⃣ Transform
    df_t = transform_data(df)

    # 3️⃣ Load
    if args.load:
        load_data(df_t)
        print("✅ Data loaded into database.")
    else:
        print("💡 Use --load to save to SQLite.")

if __name__ == "__main__":
    main()
