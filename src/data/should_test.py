from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from Extract import extract_datas
from Transform import change_to_no_rating
from Transform import transform_review_user_dataframe
from Transform import translate_to_english_user_dataframe
from Transform import fillnull
from Transform import change_the_NaN_user_dataframe
from Transform import concatenate_playstore_userReview
from Transform import extract_to_csv
from S3Pusher import uploadToS3

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022,3,4),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
test_with_dags = DAG('test_with_dags',
    default_args=default_args,
    description='ETL jobs for Data',
    schedule_interval ='@daily',
    catchup=False,
    tags=['example,testdags']
)

def print():
    return "Hello world!"

def extract_jobs():
    apps=extract_datas("/home/nikl/airflow/dags/googleplaystore.csv")
    reviews=extract_datas("/home/nikl/airflow/dags/googleplaystore_user_reviews.csv")
    return apps,reviews

gapps,greviews = extract_jobs()

def transform_jobs(df1,df2):
    change_to_no_rating(df1)
    transform_review_user_dataframe(df2)
    translate_to_english_user_dataframe(df2)
    fillnull(df2)
    change_the_NaN_user_dataframe(df2)
    concatenate_playstore_userReview(df1,df2)
    return extract_to_csv(df1)

def load_jobs():
    return uploadToS3("subject","/home/nikl/Transformed.csv")

start_task = DummyOperator(task_id='start_task',dag=test_with_dags)

print_dags = PythonOperator(task_id='print_dags',python_callable=print,dag=test_with_dags)

extract_dags = PythonOperator(task_id='extract_dags',python_callable=extract_jobs,dag=test_with_dags)

transform_dags = PythonOperator(task_id='transform_dags',python_callable=transform_jobs,op_args=[gapps,greviews],dag=test_with_dags)

load_dags = PythonOperator(task_id='load_dags',python_callable=load_jobs,dag=test_with_dags)

end_task = DummyOperator(task_id='end_task',dag=test_with_dags)


start_task >> print_dags >> extract_dags >> transform_dags >> load_dags >> end_task