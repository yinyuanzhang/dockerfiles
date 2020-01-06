FROM alpine:3.8

SHELL ["sh", "-euxvc"]

ONBUILD ARG GOSU_VERSION=1.10
ONBUILD RUN \
  \
  apk add --no-cache su-exec