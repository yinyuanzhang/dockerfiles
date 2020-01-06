FROM python:3.5
MAINTAINER tylenda.piotr@gmail.com

RUN apt-get update && apt-get install -y \
    libpq-dev \
    python3-numpy \
    python3-pandas \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/airflow && mkdir -p /opt/airflow/dags && mkdir -p /opt/airflow/log && mkdir -p /opt/airflow/plugins
WORKDIR /opt/airflow
ENV AIRFLOW_HOME /opt/airflow

COPY airflow/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY airflow/airflow.cfg .
COPY airflow/docker-entrypoint.sh /

VOLUME ["/opt/airflow/dags", "/opt/airflow/logs", "/opt/airflow/plugins"]

EXPOSE 8080 5555

ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]
CMD ["airflow"]
