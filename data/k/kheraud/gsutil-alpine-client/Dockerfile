FROM alpine:latest

MAINTAINER Karim Heraud <kheraud@gmail.com>

ENV GSUTIL_VERSION 4.37

WORKDIR /opt

RUN apk add --no-cache bash python2 curl tar

RUN curl -O https://pub.storage.googleapis.com/gsutil_${GSUTIL_VERSION}.tar.gz

RUN tar xzvf gsutil_${GSUTIL_VERSION}.tar.gz

RUN rm gsutil_${GSUTIL_VERSION}.tar.gz

RUN apk del curl tar

ENV PATH="/opt/gsutil:${PATH}"
