# flask

FROM alpine:latest
MAINTAINER Colin <admin@skyin.win>

RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache py3-gevent

RUN mkdir -p /www
RUN pip3 install --no-cache-dir Flask gunicorn pymysql

WORKDIR /www
EXPOSE 8000
CMD ["sh", "profile"]