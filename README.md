# 🧮 ETL Expenses Project

A simple **ETL pipeline** built with Python to extract, transform, and load expense data from a CSV file into a SQLite database.  
The project demonstrates a clean, modular approach to data automation using only standard libraries and SQLAlchemy.

---

## 🚀 Features

- **Extract**: read and optionally filter expense data from a CSV file  
- **Transform**: clean, normalize, and categorize transactions  
- **Load**: save processed data into a local SQLite database  
- **CLI Support**: run the entire pipeline with command-line arguments

---

## 🧰 Tech Stack

- Python 3.11  
- Pandas  
- SQLAlchemy  
- SQLite  

---

## 📁 Project Structure
```
etl_expenses/
├── etl/
│ ├── extract.py # Extract data from CSV
│ ├── transform.py # Clean and categorize data
│ ├── load.py # Save transformed data to SQLite
│ └── main.py # Run full ETL pipeline via CLI
│
├── data/
│ └── expenses.csv # Source data
│
├── app.db # Output database (created automatically)
├── requirements.txt
└── README.md
```
## ⚙️ Usage
1️⃣ Install dependencies
```
pip install -r requirements.txt
```
2️⃣ Run full ETL
```
python -m etl.main --since 2025-10-15 --load
3️⃣ Example output
Extracted 3 rows from data/expenses.csv
Transformed 3 rows.
Loaded 3 rows into 'expenses_clean' table.
✅ Data loaded into database.
```
## 🗄️ Inspect data in SQLite
```
sqlite3 app.db "SELECT * FROM expenses_clean;"
Result:
2025-10-15 | 45.6 | Restaurant dinner | Food
2025-10-16 | 12.3 | Bus ticket | Transport
2025-10-16 | 1500 | Rent | Housing
```
## Future Improvements

- Validation for missing/invalid data
- Multiple CSV sources
- Aggregated reports (category totals, monthly summary)

## Author
Natalia Balla  
Python Developer | Data Engineer  
https://github.com/natballa
