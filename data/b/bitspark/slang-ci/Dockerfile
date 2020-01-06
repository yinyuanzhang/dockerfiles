FROM python:3.7.0-stretch
MAINTAINER Julian Matschinske (Bitspark) <julian.matschinske@bitspark.de> (@jmatschinske)

RUN apt-get update

# General
RUN apt-get install -y openssl git zip tar musl-dev curl wget software-properties-common gnupg osslsigncode

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

# Install Go
RUN wget https://dl.google.com/go/go1.11.1.linux-amd64.tar.gz
RUN tar -xvf go1.11.1.linux-amd64.tar.gz && mv go /usr/local
ENV GOROOT /usr/local/go
ENV GOPATH /gopath
ENV GOBIN /gopath/bin
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

# Install ghr
RUN go get github.com/tcnksm/ghr
