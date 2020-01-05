FROM alpine:latest
# Description: Dockerfile with AWS ClI
MAINTAINER me@hynespm.com

RUN apk update && apk add python \
                py-pip zip\
                && pip install awscli \
                && pip install --upgrade pip \
                && pip install slackclient \
                && pip install requests
