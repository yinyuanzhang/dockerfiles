FROM python:2.7.10
MAINTAINER Larry Liang <ptolemy428@gmail.com>

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install -y tmux \
    && apt-get install -y jq

RUN pip install boto3

WORKDIR /root/src
