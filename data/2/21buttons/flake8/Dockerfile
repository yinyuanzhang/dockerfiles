FROM python:3.7-alpine

ENV FLAKE8_VERSION 3.7.8

RUN pip install flake8==$FLAKE8_VERSION

RUN set -ex && mkdir /app

WORKDIR /app

ENTRYPOINT ["flake8"]
