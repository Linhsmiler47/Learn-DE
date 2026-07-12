from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="talend_myjob_dag", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    # "scripts" folder is under config folder dag 
    """
    Add a space after the script name when directly calling a .sh script with the bash_command argument – for example bash_command="my_script.sh ". 
    This is because Airflow tries to apply load this file and process it as a Jinja template to it ends with .sh, 
    which will likely not be what most users want.
    """
    talend_job = BashOperator(task_id="talend_job", bash_command= r"sh /opt/airflow/talend-jobs/airflow_jobs/deploy_demo_airflow/deploy_demo_airflow_run.sh ")

    @task()
    def airflow():
        print("task talend_job is run successful")

    # Set dependencies between tasks
    talend_job >> airflow()