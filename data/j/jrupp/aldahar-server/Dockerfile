FROM ubuntu:wily
MAINTAINER Justin Rupp <dither@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN \
apt-get -qq update && \
apt-get -qqy --force-yes install \
    libboost-all-dev \
    g++ \
    vim \
    git \
    curl \
    libssl-dev \
    libmysqlclient-dev \
    CMake && \
rm -rf /var/lib/apt/lists/*

ENTRYPOINT /bin/bash


