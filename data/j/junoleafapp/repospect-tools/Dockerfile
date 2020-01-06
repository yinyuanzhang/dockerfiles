FROM ubuntu:18.04

ARG S3_BUCKET_NAME

ARG REPO_DOWNLOAD_URL
ARG OAUTH_ACCESS_TOKEN

ARG DATABASE_USER
ARG DATABASE_PASS
ARG DATABASE_HOST
ARG DATABASE_PORT

# ASCII Sucks
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y python3-dev python3-pip mysql-server libmysqlclient-dev libxml2-dev libxslt1-dev wget curl
RUN python3 -V

# Install Requirements
WORKDIR /etc
ADD ./requirements.txt /etc/requirements.txt
RUN pip3 install -r requirements.txt

# Download File
WORKDIR /opt/
#RUN curl -o /tmp/repo.zip "${REPO_DOWNLOAD_URL}" -d "access_token=${OAUTH_ACCESS_TOKEN}"
RUN mkdir -p /opt/repospector/
ADD ./repospector ./repospector

WORKDIR /opt/repospector/


