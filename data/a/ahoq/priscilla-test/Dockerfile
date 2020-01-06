
FROM python:3.6

USER root

WORKDIR /app

ADD . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get -y install redis-server

RUN python3.6 -m pip install redis

EXPOSE 8080

ENV NAME World

CMD ["python3", "application.py"]
