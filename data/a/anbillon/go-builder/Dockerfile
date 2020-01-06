# A image to build golang builder.
FROM golang:alpine
MAINTAINER Anbillon Team <anbillonteam@gmail.com>
RUN apk update && \
    apk add --no-cache bash git curl openssh gcc musl-dev make && \
    go get -u -v github.com/gobuffalo/packr/packr && \
    go get -u -v github.com/golang/dep/cmd/dep
