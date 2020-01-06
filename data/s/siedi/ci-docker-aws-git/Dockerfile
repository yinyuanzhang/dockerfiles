FROM docker:latest

RUN apk add --no-cache --update \
    git \
    python \
    py-pip \
    jq \
    openssh-client \
    && pip --no-cache-dir install awscli \
    && apk del py-pip \
    && rm -rf /var/cache/apk/*
