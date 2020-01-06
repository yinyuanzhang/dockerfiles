FROM docker:latest

MAINTAINER "Jeremy CURNY" <jeremy.curny.pro@gmail.com>

ARG DEBIAN_FRONTEND=noninteractive

RUN apk update \
    && apk add --no-cache --quiet bash curl gcc git libffi-dev libressl-dev make musl-dev python python2-dev zip \
    && rm -rf /var/cache/apk/*

RUN curl -fsSL https://bootstrap.pypa.io/get-pip.py | python

RUN pip install urllib3===1.22 \
    && pip install awscli docker-compose
