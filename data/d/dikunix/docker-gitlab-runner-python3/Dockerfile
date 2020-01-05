FROM dikunix/docker-gitlab-runner-alpine:latest

MAINTAINER Oleks <oleks@oleks.info>

USER root

RUN apk --no-cache add python3 python3-dev

RUN apk --no-cache --virtual .build-dependencies add alpine-sdk

RUN pip3 install --upgrade pip && \
  pip3 install \
  mypy \
  flake8 \
  pytest \
  pexpect \
  hypothesis

RUN apk del .build-dependencies

USER docker
