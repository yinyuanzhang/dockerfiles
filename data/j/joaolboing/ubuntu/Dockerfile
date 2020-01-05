FROM ubuntu:14.04

MAINTAINER joaolboing <joaolboing@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV TZ='America/Sao_Paulo'

RUN apt-get update && \
apt-get install -y --no-install-recommends ca-certificates && \
apt-get -y dist-upgrade && \
apt-get autoremove -y && \
apt-get clean all && \
rm -rf /var/lib/apt/lists/*
