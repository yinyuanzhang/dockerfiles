FROM python:alpine
MAINTAINER Jens Heidbüchel <forkedjensh+dockerhub@mailbox.org>

ENV REFRESHED_AT 2018-09-03

RUN apk add git openssh-client openssl ca-certificates linux-headers qemu-img libffi-dev openssl-dev build-base krb5 krb5-dev
ADD requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt
