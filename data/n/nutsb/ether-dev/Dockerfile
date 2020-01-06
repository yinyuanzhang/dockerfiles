# Name:goether
FROM ubuntu:18.04

LABEL maintainer="nutsbest@protonmail.com"

ENV PATH=/usr/lib/go-1.10/bin:$PATH
ENV APP=/app

RUN \
  apt-get update && apt-get upgrade -q -y && \
  apt-get install -y --no-install-recommends golang-1.10 git make gcc libc-dev ca-certificates vim && \
  mkdir /go-ethereum && apt-get clean 

VOLUME $APP

EXPOSE 7545 8545 30303
EXPOSE 30301/udp
