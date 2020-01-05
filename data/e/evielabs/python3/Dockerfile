FROM python:3.7.3-slim-stretch

COPY stretch-backports.list /etc/apt/sources.list.d/

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    build-essential curl libpq-dev

RUN apt-get -t stretch-backports install -y librdkafka-dev

COPY requirements.txt /tmp/
RUN pip install --upgrade -r /tmp/requirements.txt
