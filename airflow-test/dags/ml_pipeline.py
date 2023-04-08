from datetime import timedelta
import pendulum
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.time_delta import TimeDeltaSensor

# DEFINE FUNCTIONS
source_file = './raw/data.csv'

def read_data(source_file):
    print('Data read successfully')

def transformation():
    print('Data transformed')

def feature_encoding():
    print('Encoded features')

def output():
    print('Data saved to x location')

def task_failure_alert():
    print("Task has failed")

# DEFINE DAG PROPERTIES 

default_args = {
    'owner': 'Zhaoxue Li',
    'start_date': pendulum.datetime(2023, 4, 1, 1, 1),
    'depends_on_past': False,
    'email': ['ml-alerts@company.com'],
    'email_on_failure': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=30)
}

dag = DAG(
    'ml-etl-pipeline',
    default_args=default_args,
    schedule_interval='*/5 * * * *', # every 5 minutes
    catchup=False,
    tags=['ml','etl']
)

# DEFINE THE TASKS
wait_for_upstream = TimeDeltaSensor(
    task_id="wait_for_upstream_data_to_arrive",
    delta=timedelta(minutes=1),
    dag=dag,
)

read_data_task = PythonOperator(
    task_id='reading-data',
    python_callable=read_data,
    op_kwargs={'source_file':source_file},
    on_failure_callback=task_failure_alert,
    dag=dag,
)

transform_data_task = PythonOperator(
    task_id='transform-data',
    python_callable=transformation,
    on_failure_callback=task_failure_alert,
    dag=dag,
)

encoding_task = PythonOperator(
    task_id='encoding-features',
    python_callable=feature_encoding,
    on_failure_callback=task_failure_alert,
    dag=dag,
)

output_task = PythonOperator(
    task_id='write-to-destination',
    python_callable=output,
    on_failure_callback=task_failure_alert,
    dag=dag,
)

# DEFINE TASK RUNNING SEQUENCE
wait_for_upstream >> read_data_task >> transform_data_task >> encoding_task >> output_task