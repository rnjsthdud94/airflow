import pendulum
from airflow.models.dag import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["example"],
) as dag:
    
    @task(task_id = "print_task_1")
    def print_context(some_input):
        print(some_input)
    
    run_this = print_context('task_decorator 실행')