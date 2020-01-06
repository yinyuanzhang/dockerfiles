FROM python:3.6.4-alpine
MAINTAINER tilldettmering@gmail.com+

ENV SHELL /bin/bash

ADD requirements.txt app/

WORKDIR app/

RUN set -ex && \
    apk update && \
    apk add --no-cache build-base postgresql-dev && \
    pip --no-cache-dir install -r requirements.txt
