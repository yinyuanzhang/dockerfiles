FROM ubuntu:16.04
MAINTAINER Magic
RUN apt-get update && \
    apt-get install python python-pip vim cron -y && \
    pip install --upgrade pip && \
    pip2 install aliyun-log-python-sdk aliyun-log-cli && \
    pip2 install aliyun-python-sdk-core && \
    pip2 install aliyun-python-sdk-sas && \
    pip2 install supervisor
