FROM elixir:1.9-alpine

RUN apk add --no-cache git docker && \
  apk add --no-cache \
  --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main \
  --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community \
  gcc make musl-dev rust cargo
