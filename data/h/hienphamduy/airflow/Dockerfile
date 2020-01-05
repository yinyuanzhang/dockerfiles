FROM python:3.6-buster

RUN apt update && apt install sudo -y

RUN adduser airflow \
    && echo "airflow ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/airflow \
    && chmod 0440 /etc/sudoers.d/airflow

WORKDIR /opt/airflow

# Finally install the requirements from the latest sources
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

RUN sudo apt install libsnappy-dev -y

COPY extra_requirements.txt ./extra_requirements.txt
RUN pip install --no-cache-dir -r ./extra_requirements.txt

COPY --chown=airflow:airflow entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# set default timezone
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime

EXPOSE 8080
ENV AIRFLOW_HOME=/home/airflow/airflow

RUN mkdir -p $AIRFLOW_HOME
RUN chown airflow:airflow $AIRFLOW_HOME

USER airflow

WORKDIR $AIRFLOW_HOME

ENTRYPOINT ["/entrypoint.sh"]

CMD ["--help"]
