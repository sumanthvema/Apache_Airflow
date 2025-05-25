import pandas as pd
import os
def aggregate_sales():

    OUTPUT_PATH = "/usr/local/airflow/data/output/"
    coffee_output = os.path.join(OUTPUT_PATH, "coffee_sales.csv")
    daily_sales_output = os.path.join(OUTPUT_PATH, "dailY_sales.csv")
    payment_sales_output = os.path.join(OUTPUT_PATH, "payment_sales.csv")
    df = pd.read_csv("/usr/local/airflow/data/processed/merged_sales_data.csv")

    df['money'] = pd.to_numeric(df['money'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

    coffee_sales = df.groupby('coffee_name')['money'].sum().reset_index()
    daily_sales = df.groupby(df['date'].dt.date)['money'].sum().reset_index()
    payment_sales = df.groupby('cash_type')['money'].sum().reset_index()

    # Save reports
    coffee_sales.to_csv(coffee_output, index=False)
    daily_sales.to_csv(daily_sales_output, index=False)
    payment_sales.to_csv(payment_sales_output, index=False)
