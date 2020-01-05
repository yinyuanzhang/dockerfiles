FROM python:3.6.6-stretch

ENV AIRFLOW_HOME=/root/airflow
ENV AIRFLOW_GPL_UNIDECODE=yes

RUN pip install apache-airflow[gcp_api] oauth2client gcloud pandas-gbq

RUN airflow initdb

ADD airflow.cfg /root/airflow/airflow.cfg

RUN airflow variables -s gcp_project project
RUN airflow variables -s gce_zone zone
