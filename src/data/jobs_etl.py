from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from data.S3Pusher import uploadToS3
from Extract import extract_rates
from Extract import extract_datas


default_args = {
    'owner': 'airflow',
    'start_date':'airflow.utils.dates.days_ago(2)',
    'depends_on_past': False,
    'email':['hei.nykoloina.2@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1)
}
jobs_etl_dags = DAG(
    'jobs_etl_dags',
    default_args=default_args,
    description='ETL jobs for Data',
    schedule_interval ='@daily',
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['example,jobsetl']
)

def extract_datas():
    rates = extract_rates("https://v6.exchangerate-api.com/v6/85a67b762af150352ffb7e6a/latest/USD")
    apps = extract_datas("googleplaystore.csv")
    reviews = extract_datas("googleplaystore_user_reviews.csv")
    return rates,apps,reviews

rates,apps,reviews = extract_datas()


def print_hello():
    return 'Hello world!'

start_task = DummyOperator(task_id='start_task',dag=hello_world_dag)
hello_world_task = PythonOperator(task_id='hello_world_task',python_callable=print_hello,dag=hello_world_dag)
end_task = DummyOperator(task_id='end_task', dag=hello_world_dag)

start_task >> hello_world_task >> end_task
