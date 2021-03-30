from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
# Comentario
import mydag.src.functions as src

dag = DAG(
    dag_id="test-dag",
    start_date=datetime(2021, 1, 1),
    schedule_interval=None
)

t1 = PythonOperator(
    task_id="test-task",
    python_callable=src.myfunc,
    dag=dag
)

t1
