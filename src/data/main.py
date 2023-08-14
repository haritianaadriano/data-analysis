from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from Extract import extract_rates
from Extract import extract_datas


default_args = {
    'owner': 'airflow',
    'start_date':'airflow.utils.dates.days_ago(2)',
    'end_date':'datetime()',
    'depends_on_past': False,
    'email':['hei.nykoloina.2@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}
dag_python = DAG(
    dag_id = "pythonoperator_demo",
    default_args=default_args,
    schedule_interval = '@daily',
    dagrun_timeout=timedelta(minutes=60),
    description='pipeline for data project',
    start_date = airflow.utils.dates.days_ago(1)
)  


def main():
    apps = extract_datas('googleplaystore.csv')
    reviews = extract_datas('googleplaystore_user_reviews.csv')
    rates = extract_rates('https://v6.exchangerate-api.com/v6/85a67b762af150352ffb7e6a/latest/USD')

main()
