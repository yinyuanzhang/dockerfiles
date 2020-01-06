FROM golang:1.13.5-alpine3.11

RUN apk update && apk add openssl git

# glide
RUN VERSION=0.13.3 && \
    FILE=glide-v$VERSION-linux-amd64.tar.gz && \
    URL=https://github.com/Masterminds/glide/releases/download/v$VERSION/$FILE && \
    echo ========== && \
    echo FILE=$FILE && \
    echo ========== && \
    mkdir -p /opt/glide && \
    cd /opt/glide && \
    wget $URL && \
    tar xvfpz $FILE && \
    rm $FILE && \
    ln -s /opt/glide/linux-amd64/glide /usr/local/bin/glide

# go dep / https://github.com/golang/dep/releases/download/v0.5.4/dep-linux-amd64
RUN VERSION=0.5.4 && \
    FILE=dep-linux-amd64 && \
    URL=https://github.com/golang/dep/releases/download/v$VERSION/$FILE && \
    echo ========== && \
    echo FILE=$FILE && \
    echo ========== && \
    mkdir -p /opt/dep && \
    cd /opt/dep && \
    wget $URL && \
    chmod 755 $FILE && \
    ln -s /opt/dep/$FILE /usr/local/bin/dep
