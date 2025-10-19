import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and enrich expense data.
    - Drop empty rows
    - Normalize columns
    - Add a category based on description
    """
    df = df.dropna(subset=["amount", "description"])
    df["amount"] = df["amount"].astype(float)

    def categorize(desc):
        d = desc.lower()
        if "food" in d or "restaurant" in d:
            return "Food"
        elif "transport" in d or "uber" in d:
            return "Transport"
        elif "rent" in d:
            return "Housing"
        else:
            return "Other"

    df["category"] = df["description"].apply(categorize)
    print(f"Transformed {len(df)} rows.")
    return df
