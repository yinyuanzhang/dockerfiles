FROM frolvlad/alpine-glibc

WORKDIR /tmp

ADD https://github.com/rancher/rancher-compose/releases/download/v0.7.4/rancher-compose-linux-amd64-v0.7.4.tar.gz /tmp/

RUN tar xzvf rancher-compose-linux-amd64-v0.7.4.tar.gz && \
    mv rancher-compose-v0.7.4/rancher-compose /usr/bin && \
    rm -Rf /tmp/*
