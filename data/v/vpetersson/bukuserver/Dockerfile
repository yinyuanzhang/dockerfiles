FROM python:alpine

MAINTAINER Ameya Shenoy "shenoy.ameya@gmail.com"

COPY . /Buku

RUN set -ex \
  && apk add --no-cache --virtual .build-deps \
    gcc \
    openssl-dev \
    musl-dev \
    libffi-dev \
  && pip install -U --no-cache-dir \
    pip \
    gunicorn \
    /Buku[server] \
  && apk del .build-deps \
  && rm -rf /Buku

EXPOSE 5001
CMD timeout 7200 gunicorn --bind 0.0.0.0:5001 "bukuserver.server:create_app()"

