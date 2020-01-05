# This docker file contains build environment
FROM debian:latest
MAINTAINER Sergii Kusii <kusii.sergii@apriorit.com>

ENV DEBIAN_FRONTEND noninteractive

#uncomment all src repositories
RUN sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list && sed -i -- 's/# deb-src/deb-src/g' /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y linux-headers-4.9.0-6-all linux-image-4.9.0-6-amd64 && \
    apt-get install -y cmake build-essential && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*
