FROM alpine:3.4
MAINTAINER dgarros@gmail.com

ARG ver_ansible=2.2.0.0

RUN mkdir /source &&\
    mkdir /project

WORKDIR /source
ADD requirements.txt requirements.txt

RUN apk update && apk add ca-certificates &&\
    apk add build-base make gcc g++ python-dev py-pip openssl-dev curl libffi-dev &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    pip install -q ansible==$ver_ansible &&\
    apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

COPY roles /etc/ansible/roles

WORKDIR /project
