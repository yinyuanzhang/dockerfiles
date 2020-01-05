FROM ubuntu:18.04

MAINTAINER Eldridge Henley version 1.0

###S3 Keys###
ENV ACCESS_KEY=$ACCESS_KEY
ENV SECRET_KEY=$SECRET_KEY
###Name of the etcd master###
ENV MASTER_NAME=$MASTER_NAME
###How often it will run###
ENV INTERVAL=$INTERVAL

COPY ./etcd_backup_script ./
###Installing pre-reqs###
RUN apt-get update
RUN apt-get install -y build-essential curl git m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libexpat-dev libncurses-dev zlib1g-dev wget
RUN apt-get install -y nodejs-dev node-gyp libssl1.0-dev

RUN apt-get install -y npm
RUN npm install -g s3-cli
RUN apt-get install -y python-pip

RUN apt-get clean

###Making dirs and setting up etcd-dump###
RUN mkdir ~/etcd_dump && \
    mkdir /etcd_backups && \
    mkdir /etcd_backups/data && \
    mkdir /etcd_backups/data-events

CMD ./etcd_backup_script
