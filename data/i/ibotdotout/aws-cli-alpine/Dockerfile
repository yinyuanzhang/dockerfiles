FROM python:alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN pip install awscli
RUN pip install awsebcli
