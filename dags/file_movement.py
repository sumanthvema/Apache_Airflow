# movement.py
import os
import pandas as pd

# Define folder paths
RAW_PATH = "/usr/local/airflow/data/raw/"
PROCESSED_PATH = "/usr/local/airflow/data/processed/"
OUTPUT_FILE = os.path.join(PROCESSED_PATH, "merged_sales_data.csv")

def merge_excel_files():
    # Ensure the processed folder exists
    os.makedirs(PROCESSED_PATH, exist_ok=True)
    all_data = []  # List to collect DataFrames
    # Loop through each file in raw folder
    for file in os.listdir(RAW_PATH):
         print("Looking for files in raw directory", RAW_PATH)
         if file.endswith('.csv'):
             file_path = os.path.join(RAW_PATH, file)
             df = pd.read_csv(file_path)
             all_data.append(df)
    # if not os.path.exists(RAW_PATH):
    #     print(f"RAW_PATH does not exist: {RAW_PATH}")
    #     return
    # files = os.listdir(RAW_PATH)
    # if not files:
    #     print("No files found in RAW_PATH.")

    # for file in files:
    #     print(f"Checking file: {file}")
    #     if file.endswith('.csv'):
    #         file_path = os.path.join(RAW_PATH, file)
    #         print(f"Reading file: {file_path}")
    #         try:
    #             df = pd.read_csv(file_path)
    #             all_data.append(df)
    #         except Exception as e:
    #             print(f"Error reading {file_path}: {e}")

    # Combine all data
    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        merged_df.to_csv(OUTPUT_FILE, index=False)

    else:
        print("No files found in the raw directory.")
