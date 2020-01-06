FROM python:3.6-alpine

MAINTAINER Laurent RICHARD <easylo@gmail.com>

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh zip unzip jq gettext
    
RUN ["pip", "install", "awscli"]
