from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


# Python functions executed by the tasks
def greet():
    print("Hello from Apache Airflow!")
    print("My first DAG using PythonOperator.")


def process_data():
    numbers = [10, 20, 30, 40, 50]
    total = sum(numbers)

    print(f"Numbers: {numbers}")
    print(f"Total: {total}")


def finish():
    print("All tasks completed successfully!")


# Define the DAG
with DAG(
    dag_id="python_operator_demo",
    description="A sample DAG using PythonOperator",
    tags=["demo", "pythonoperator"],
) as dag:

    task_greet = PythonOperator(
        task_id="greet",
        python_callable=greet,
    )

    task_process = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )

    task_finish = PythonOperator(
        task_id="finish",
        python_callable=finish,
    )

    # Define task execution order
    task_greet >> task_process >> task_finish