## Base ubuntu image with "normal" utils

FROM ubuntu:16.04

ENV TERM xterm
ENV LANG C.UTF-8

RUN apt-get -y update && \
    apt-get -y install curl wget dnsutils dstat telnet bash vim ca-certificates procps gzip unzip zip bzip2 git && \
    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/cache/apt/archives/* && \
    rm -rf /var/lib/apt/lists/*
