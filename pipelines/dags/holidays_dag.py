from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import requests
import json
from holidays_etl import download_data, processing_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 12, 10),
    'email': ['ujkanoviczuhra@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'feiertage_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

    
run_etl1 = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag,
)

run_etl2 = PythonOperator(
    task_id='processing_data',
    python_callable=processing_data,
    dag=dag,
)
run_etl2.set_upstream(run_etl1)
#run_etl1 >> run_etl2