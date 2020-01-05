FROM alpine:3.10
MAINTAINER Stefano Marinelli <stefano@dragas.it>

RUN apk add --no-cache python3 python3-dev libffi-dev py3-cffi py3-zmq && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev postgresql-libs 

RUN pip3 install --upgrade pip && pip3 install heralding && rm -Rf /root/.cache/ && mkdir /heralding

ENTRYPOINT cd /heralding && heralding
