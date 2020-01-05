FROM python:3-alpine

MAINTAINER Jeff Cox <jeffrcox@cisco.com>

COPY build.sh build.sh
COPY requirements.txt requirements.txt
RUN ./build.sh && \
    rm -rf build.sh requirements.txt
#RUN apk add --no-cache curl &&\
#  curl -fsL \
#       https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VER/dockerize-linux-amd64-$DOCKERIZE_VER.tar.gz | \
#       tar -C /usr/local/bin -zxvof - && \
#  pip3 install falcon \
#  gunicorn \
#  markdown \
#  kafka-python \
#  pymongo


COPY ./src /api
WORKDIR /api
