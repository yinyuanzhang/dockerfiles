FROM python:3.8.1-alpine3.11

MAINTAINER  jon m herolo Ltd.

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual build-deps \
      gcc libc-dev linux-headers postgresql-dev git

WORKDIR /backend

COPY requirements requirements

RUN pip install -U pip

RUN pip install -r requirements/dev.txt

RUN apk del build-deps

WORKDIR /src

COPY src src
