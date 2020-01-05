FROM alpine:latest
MAINTAINER Jason Hyde <docker@2bad.me>

ENV AWSCLI_VERSION "1.15.65"
ENV PACKAGES "tar gzip git openssl ca-certificates groff less jq python py-pip"

RUN apk add --update $PACKAGES \
    && pip install awscli==$AWSCLI_VERSION \
    && apk --purge -v del py-pip \
    && rm -rf /var/cache/apk/*
