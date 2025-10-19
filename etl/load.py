from pathlib import Path
from sqlalchemy import create_engine, text
import pandas as pd

def get_engine():

    db_path = Path(__file__).resolve().parent.parent / "app.db"
    return create_engine(f"sqlite:///{db_path}")

def load_data(df: pd.DataFrame, table_name: str = "expenses_clean", if_exists: str = "replace"):
#load to sqllite
    engine = get_engine()

    # date to char
    if "date" in df.columns:
        df = df.copy()
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)

        try:
            conn.execute(text(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_date ON {table_name}(date);"))
            conn.execute(text(f"CREATE INDEX IF NOT EXISTS idx_{table_name}_category ON {table_name}(category);"))
        except Exception as e:
            print(f"⚠️  Couldn't create indexes: {e}")

    print(f"Loaded {len(df)} rows into '{table_name}' table.")
