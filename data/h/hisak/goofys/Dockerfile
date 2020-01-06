FROM golang:1.12-alpine

ENV GOOFYS_VERSION=v0.21.0
WORKDIR /go/src/github.com/kahing/goofys

RUN apk --no-cache add build-base git make && \
    git clone https://github.com/kahing/goofys -b ${GOOFYS_VERSION} --depth 1 --recursive . && \
    make build install && strip -s /go/bin/goofys

FROM alpine:3.10

RUN apk --no-cache add fuse

COPY --from=0 /go/bin/goofys /usr/local/bin