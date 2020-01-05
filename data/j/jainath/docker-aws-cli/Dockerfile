FROM ubuntu:16.04

RUN apt-get update
ENV DOCKERVERSION=18.06.1-ce

RUN apt-get install curl python python-pip -y
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
  && mv docker-${DOCKERVERSION}.tgz docker.tgz \
  && tar xzvf docker.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker.tgz

RUN pip install awscli
RUN apt-get install build-essential
