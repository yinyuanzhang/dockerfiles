FROM golang:1.13.4-alpine as builder

RUN apk add --update --no-cache build-base curl git upx && \
  rm -rf /var/cache/apk/*

RUN go get -d github.com/envoyproxy/protoc-gen-validate && \
  cd /go/src/github.com/envoyproxy/protoc-gen-validate && make build && \
  mv /go/bin/protoc-gen-* /usr/local/bin/

FROM uber/prototool

COPY --from=builder /usr/local/bin /usr/local/bin

RUN apk add --update --no-cache build-base curl jq openssh-client && rm -rf /var/cache/apk/*
