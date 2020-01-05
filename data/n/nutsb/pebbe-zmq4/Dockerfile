# NAME: pebbezmq4
FROM golang:1.11

LABEL maintainer="nutsbest@protonmail.com"
ENV GOPATH=/go
ENV GOROOT=/usr/local/go

RUN \
    apt-get update && apt-get install -y vim && \
    echo "deb http://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/Debian_9.0/ ./" >> /etc/apt/sources.list && \
    wget https://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/Debian_9.0/Release.key -O- | apt-key add && \
    mkdir -p $GOPATH/src && \
    apt-get install -y libzmq3-dev && \
    go get github.com/pebbe/zmq4
