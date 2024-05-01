from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator", 
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz = "Asia/Seoul"), 
    catchup=False
) as dag:
    send_email_task1 = EmailOperator(
        task_id = 'send_email_task1', 
        to = 'choice4116@gmail.com',
        subject='Airflow 성공메일',
        html_content='조현석 사랑한다',
    )

    send_email_task2 = EmailOperator(
        task_id = 'send_email_task2', 
        to = 'rnjsthdud94@naver.com',
        subject='Airflow 성공메일',
        html_content='청약통장에 돈 납입하거라',
    )

    send_email_task1 >> send_email_task2