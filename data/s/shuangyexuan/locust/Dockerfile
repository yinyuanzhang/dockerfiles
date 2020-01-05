FROM python:3.7.3-alpine

WORKDIR /usr/src/app

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories; apk add gcc libc-dev zeromq-dev python3-dev libffi libffi-dev

RUN python -m pip install cffi locustio==0.11.0 jsonpath pyyaml geventhttpclient

RUN find / -name *.pyc -delete; rm -rf /root/.cache/pip/*

RUN apk del gcc libc-dev python3-dev libffi libffi-dev
