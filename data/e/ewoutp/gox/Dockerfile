FROM golang:1.12.0-alpine

RUN apk add -U git && \
    go get github.com/mitchellh/gox && \
    apk del -r git
