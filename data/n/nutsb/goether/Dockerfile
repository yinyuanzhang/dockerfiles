# Name:goether
FROM ubuntu:18.04

LABEL maintainer="nutsbest@protonmail.com"

ENV PATH=/usr/lib/go-1.10/bin:$PATH
ENV APP=/app

RUN \
  apt-get update && apt-get upgrade -q -y && \
  apt-get install -y --no-install-recommends golang-1.10 git make gcc libc-dev ca-certificates vim && \
  git clone --depth 1 --branch release/1.8 https://github.com/ethereum/go-ethereum && \
  (cd go-ethereum && make geth) && \
  cp go-ethereum/build/bin/geth /geth && \
  apt-get remove -y golang-1.9 git make gcc libc-dev && apt autoremove -y && apt-get clean && \
  rm -rf /go-ethereum

VOLUME $APP

EXPOSE 7545 8545 30303
EXPOSE 30301/udp
