FROM python:2

MAINTAINER NI YUANDONG & LI YANZHE

WORKDIR /usr/src/app

ADD ./slaveNode ./slaveNode

RUN pip install -U pip \
    && pip install scrapy_redis bs4 pymongo

WORKDIR slaveNode/slaveNode
