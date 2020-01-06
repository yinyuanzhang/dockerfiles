FROM portoleks/debian:v9.2_0.1

MAINTAINER oleks <oleks@oleks.info>

USER root

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
    build-essential \
    flex \
    bison \
    libc6-dev \
    libfl-dev \
    gcc-multilib \
    git && \
  rm -rf /var/lib/apk/lists/*

USER docker

RUN mkdir /home/docker/data/
WORKDIR /home/docker/data/
