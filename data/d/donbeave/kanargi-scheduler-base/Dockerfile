FROM openjdk:11.0.1-jre-slim-sid

MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
               curl \
               iputils-ping \
    && rm -rf /var/lib/apt/lists/* \
              /tmp/*
