|made-with-python|

.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

============================
Airflow basic tutorial
============================

* We need to add airflow as package in poetry @apache-airflow together with other dependencies 
because they already exists in our pyproject.toml all you need to do is::

     poetry install

Gunicorn (Python WSGI HTTP Server for UNIX) and Airflow are both installed in the virtualenv.

* Set Up Airflow Default Home::

     export **AIRFLOW_HOME**=/x/x/x/x/airflow

* Activate airflow source::

     source /x/x/x/x/.venv/bin/activate  
     

* Change dags folder in airflow.cfg::

     dags_folder = /x/x/x/x/pipelines/dags

* Start airflow webserver::

     airflow  webserver

* To get the time Airflow is spending loading Dags, run the command::

     airflow list_dags -r

* Airflow allows you to easily test each task individually using the syntax::

     airflow test feiertage_dag download_data Year-Month-day
     airflow test feiertage_dag processing_data Year-Month-day