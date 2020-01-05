FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python python-pip curl
RUN pip install awscli --upgrade --user
ENV PATH /root/.local/bin:$PATH
