FROM golang:1.11.2-alpine
RUN apk add --no-cache ca-certificates  \
  && apk --update add pcre-dev openssl-dev \
  && apk add --virtual build-dependencies build-base curl git mercurial \
  && mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

RUN curl -SLO https://github.com/golang/dep/releases/download/v0.5.0/dep-linux-amd64 \
  && mv dep-linux-amd64 /go/bin/dep \
  && chmod +x /go/bin/dep
