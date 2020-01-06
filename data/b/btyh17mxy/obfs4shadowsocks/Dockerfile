FROM ubuntu:xenial

ENV DEBIAN_FRONTEND noninteractive
ENV DEPENDENCIES git-core golang curl python3.5
ENV GOPATH /opt/go
ENV PTPROXY /opt/ptproxy/

RUN mkdir -p $PTPROXY
RUN mkdir -p $GOPATH

RUN apt-get update && apt-get -y install $DEPENDENCIES && rm -rf /var/lib/apt/lists/*
RUN go get git.torproject.org/pluggable-transports/obfs4.git/obfs4proxy

ADD ptproxy $PTPROXY
ADD socks.py $PTPROXY
ADD config.json /etc/obfs4/config.json
ADD entrypoint.sh /entrypoint.sh

WORKDIR $PTPROXY

ENTRYPOINT ["/entrypoint.sh"]
