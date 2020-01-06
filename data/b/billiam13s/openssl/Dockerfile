FROM alpine:latest

RUN apk --no-cache add openssl

COPY docker-entrypoint /usr/local/bin/

WORKDIR /ssl

VOLUME /ssl

ENTRYPOINT ["docker-entrypoint"]
