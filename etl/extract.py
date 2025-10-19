import pandas as pd
from pathlib import Path
import argparse

def extract_data(file_path: str = "../data/expenses.csv", since: str | None = None) -> pd.DataFrame:
    """
    Extract step of ETL pipeline.
    Reads expense data from CSV and optionally filters by date >= since.
    """
    path = Path(__file__).resolve().parent.parent / "data" / "expenses.csv"
    df = pd.read_csv(path)

    # to date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if since:
        since_date = pd.to_datetime(since)
        df = df[df["date"] >= since_date]

    print(f"Extracted {len(df)} rows from {path}")
    print(df)
    return df


def main():
    parser = argparse.ArgumentParser(description="Extract data from CSV")
    parser.add_argument("--since", type=str, help="Filter data from this date (YYYY-MM-DD)")
    args = parser.parse_args()

    extract_data(since=args.since)


if __name__ == "__main__":
    main()
