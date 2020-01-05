FROM alpine:latest

RUN apk add --update \
    python \
    curl \
    jq \
    py2-pip && \
    adduser -D aws

WORKDIR /home/aws

RUN mkdir aws && \
    pip install --upgrade pip && \
    pip install awscli

USER aws
