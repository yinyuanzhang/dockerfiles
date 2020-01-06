FROM debian:jessie
MAINTAINER mail@arnoldbechtoldt.com

COPY build /build

RUN \
  /bin/bash /build && \
  rm /build

USER ci
