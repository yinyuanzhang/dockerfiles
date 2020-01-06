FROM ubuntu:18.04

MAINTAINER Michael Yuen <michael.yuen@mac.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -yqq && apt-get install -yqq \
      ca-certificates \
      curl \
      libc++1 \
      time \
      valgrind  \
      nginx \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -ms /bin/bash nginx

RUN mkdir -p /gameengine && \
    mkdir -p /gameengine/bin && \
    mkdir -p /gameengine/data

ENV PATH "$PATH:/gameengine/bin"

WORKDIR /gameengine/data


