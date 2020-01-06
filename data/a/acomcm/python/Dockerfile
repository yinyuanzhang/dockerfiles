FROM ubuntu:17.10

COPY ./sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y locales && apt-get clean

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get install -y python3.6 wget python3.6-dev postgresql-server-dev-9.6 vim-tiny \
    less build-essential git openssh-client supervisor libssl-dev libffi-dev && \
    apt-get clean

RUN wget -O /root/get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python3.6 /root/get-pip.py && rm -v /root/get-pip.py

ENV PYTHONUNBUFFERED 1
