# Pull base image
FROM node:8.11.3-alpine

WORKDIR /root

COPY ./vim.bash /root/

RUN apk add --update --no-cache \
        neovim \
        git \
        bash \
        curl \
        wget \
        bind-tools \
        tree \
        gcc \
        musl-dev \
        python2-dev \
        python2 && \
    python2 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip2 install --upgrade pip setuptools neovim websocket-client sexpdata && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip2 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python2 /usr/bin/python; fi && \
    rm -r /root/.cache &&\
    ./vim.bash

