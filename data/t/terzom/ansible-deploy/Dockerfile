FROM python:3.7-alpine

MAINTAINER Mike Terzo <mike@terzo.org>

ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV LANG C.UTF-8

RUN mkdir -p /src/
WORKDIR /src
COPY requirements.txt /src

RUN set -ex \
        && apk add --no-cache --virtual .fetch-deps  \
            git \
            libffi \
            openssh \
            openssl \
            rsync   \
            sshpass \
        && apk add --no-cache --virtual .build-deps  \
            curl \
            tar \
            gcc \
            libc-dev \
            libffi-dev \
            linux-headers \
            make \
            openssl-dev \
        && pip install --no-cache-dir -r requirements.txt \
        && mkdir -p /tmp/download \
        && curl -L https://download.docker.com/linux/static/stable/x86_64/docker-19.03.2.tgz | tar -xz -C /tmp/download \
        && mv /tmp/download/docker/docker /usr/local/bin/ \
        && rm -rf /tmp/download \
        && apk del .build-deps

RUN ln -s /usr/local/bin/python /usr/bin/python

COPY root /root
