FROM phusion/baseimage:latest
MAINTAINER Jonathon Leight <jonathon.leight@jleight.com>

ENV JAVA_VERSION 7u75
ENV JAVA_DEBIAN_VERSION 7u75-2.5.4-1~trusty1

RUN set -x \
  && apt-get update \
  && apt-get install -y openjdk-7-jdk="${JAVA_DEBIAN_VERSION}" \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*
