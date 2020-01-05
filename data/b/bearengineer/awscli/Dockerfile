FROM alpine

MAINTAINER Vasco Santos <jvosantos@gmail.com>

ARG AWS_VERSION="1.16.234"

RUN apk update \
 &&  apk add ca-certificates curl py-pip py2-pip \
 &&  pip install --upgrade pip "awscli==${AWS_VERSION}" \
 &&  rm /var/cache/apk/*

