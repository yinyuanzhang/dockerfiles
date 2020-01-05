FROM ubuntu:xenial


RUN apt-get -qqy update
RUN apt-get install -qqy --no-install-recommends software-properties-common wget unzip g++ gcc libc6-dev make pkg-config git curl ssh build-essential && rm -rf /var/lib/apt/lists/*
RUN add-apt-repository ppa:gophers/archive -y
RUN apt-get -qqy update
RUN apt-get install -qqy --no-install-recommends golang-1.10-go golang-1.10-race-detector-runtime && rm -rf /var/lib/apt/lists/*

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/lib/go-1.10/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH
