# Copyright 2014 The Perkeep Authors.
# Generic purpose Perkeep image, that builds the server (perkeepd)
# and the command-line clients (pk, pk-put, pk-get, and pk-mount).

# TODO: add the HEIC-supporting imagemagick to this Dockerfile too, in
# some way that's minimally gross and not duplicating
# misc/docker/heiftojpeg's Dockerfile entirely. Not decided best way.
# TODO: likewise, djpeg binary? maybe. https://perkeep.org/issue/1142

FROM buildpack-deps:stretch-scm AS pkbuild

MAINTAINER Perkeep Authors <perkeep@googlegroups.com>

ENV DEBIAN_FRONTEND noninteractive

# gcc for cgo, sqlite
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ \
        gcc \
        libc6-dev \
        make \
        pkg-config \
        libsqlite3-dev \
        ;

ENV GOLANG_VERSION 1.12.4

WORKDIR /usr/local
RUN wget -O go.tgz https://dl.google.com/go/go${GOLANG_VERSION}.linux-amd64.tar.gz
RUN echo "d7d1f1f88ddfe55840712dc1747f37a790cbcaa448f6c9cf51bbe10aa65442f5 go.tgz" | sha256sum -c -
RUN tar -zxvf go.tgz

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH

COPY . /go/src/perkeep.org/
RUN cd /go/src/perkeep.org && go run make.go --sqlite=true -v

# --- Runtime image ---

FROM debian:stretch
EXPOSE 80 443 3179 8080
CMD /bin/bash

ENV HOME /home/keepy
ENV PATH /home/keepy/bin:$PATH
WORKDIR /home/keepy

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY --from=pkbuild /go/bin/pk* /home/keepy/bin/
COPY --from=pkbuild /go/bin/perkeepd /home/keepy/bin/perkeepd
