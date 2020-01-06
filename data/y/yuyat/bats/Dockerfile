FROM alpine:3.8

RUN apk add --no-cache curl bash git && \
  cd /tmp && \
  curl -L https://github.com/sstephenson/bats/archive/v0.4.0.tar.gz | tar -xz && \
  ./bats-0.4.0/install.sh /usr/local && \
  rm -rf ./bats-0.4.0
