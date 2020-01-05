FROM golang:1.10-alpine

MAINTAINER lion.zhao <zhaoliangsyn@gmail.com>

COPY golint /bin/goflycheck

RUN apk add --no-cache git && \
    go get -u golang.org/x/lint/golint && \
    go get github.com/golang/mock/mockgen && \
    go install github.com/golang/mock/mockgen
