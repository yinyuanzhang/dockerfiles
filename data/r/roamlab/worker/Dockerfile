FROM python:3.6

RUN pip install sshtunnel psycopg2 docker==4.0.2 psutil

WORKDIR /root/roamcluster
COPY . /root/roamcluster

CMD ["python", "worker.py"]
