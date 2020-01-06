FROM python:3.7-alpine

MAINTAINER Chris Modjeska <chris@remuria.net>

RUN apk update \
  && apk add py3-psycopg2 git openssh-client \
  && pip install pipenv
