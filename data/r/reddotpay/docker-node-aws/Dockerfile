FROM node:8-alpine

RUN apk update \
    && apk add --no-cache \
        curl \
        jq \
        python-dev \
        zip \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && pip install awscli
