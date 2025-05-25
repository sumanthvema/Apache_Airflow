from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta
from file_movement import merge_excel_files
from transform import aggregate_sales


default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    dag_id='sales_report_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    merge_files = PythonOperator(
        task_id='merge_excel_files',
        python_callable=merge_excel_files    
    )

    process_data = PythonOperator(
         task_id='aggregate_sales_data',
         python_callable=aggregate_sales
     )

    send_email = EmailOperator(
         task_id='send_report',
         to='you@example.com',
         subject='Daily Sales Report',
         html_content='Attached is the sales report for today.',
         files=['/usr/local/airflow/data/output/coffee_sales.csv',
                 '/usr/local/airflow/data/output/daily_sales.csv',
                 '/usr/local/airflow/data/output/payment_sales.csv']    
    )

    # Define task dependencies
    merge_files >> process_data >> send_email
# This DAG will run daily, merging Excel files, processing the data, and sending an email with the reports.