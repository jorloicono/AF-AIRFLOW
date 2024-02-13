from airflow import DAG, Dataset
from airflow.decorators import task
from datetime import datetime

my_file = Dataset('/tmp/my_file.txt')

with DAG(
    dag_id='producer',
    schedule='@daily',
    start_date=datetime(2023, 6, 1),
    catchup=False,
):
    @task(outlets=[my_file])  
    def update_dataset():
        with open(my_file.uri, 'a+') as f:
            f.write('Producer update!')
    
    update_dataset()
