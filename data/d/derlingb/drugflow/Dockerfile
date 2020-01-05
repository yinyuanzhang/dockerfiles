# somewhat copied from:
# https://github.com/puckel/docker-airflow/blob/9f00550be9f3365215e2412419544a8301752fdd/Dockerfile

# stretch because it was hard to install psql otherwise
FROM python:3.6-stretch

ARG AIRFLOW_HOME=/app

COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && apt update -yqq \
    && apt upgrade -yqq \
    && apt install -yqq --no-install-recommends \
    # essential
        gcc \
        freetds-dev \
        jq \
    && pip install -r /app/requirements.txt
