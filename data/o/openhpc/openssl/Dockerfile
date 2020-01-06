FROM alpine:latest

LABEL maintainer="gaojingan@gmail.com"

RUN apk add --update --no-cache openssl && \
  rm -rf /var/cache/apk/*

ENTRYPOINT ["openssl"]
