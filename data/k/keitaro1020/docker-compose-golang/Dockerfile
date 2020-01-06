FROM golang:1.9-alpine as golang
FROM docker:latest
MAINTAINER keitaro1020

COPY --from=golang /usr/local/go /usr/local/go
COPY --from=golang /go/bin /go/bin

ENV PATH $PATH:/go/bin:/usr/local/go/bin
ENV GOROOT /usr/local/go
ENV GOPATH /go

RUN apk add --update git g++ python python-dev py-pip build-base \
  && rm -rf /var/cache/apk/*
RUN pip install docker-compose
