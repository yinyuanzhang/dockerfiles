FROM python:3.7-alpine

RUN apk update && apk add openssh-client bash

WORKDIR /scripts
# update pip

RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install elasticsearch
RUN pip install cassandra-driver
RUN pip install pyyaml
RUN pip install requests
RUN pip install python-logstash
RUN pip install python-dateutil
RUN pip install pytest
RUN pip install coverage
RUN pip install pytest-cov