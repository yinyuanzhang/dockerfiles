FROM alpine:3.5

MAINTAINER dijk039@gmail.com

RUN apk update \
    && apk add squid=3.5.23-r0 \
    && apk add curl \
    && rm -rf /var/cache/apk/*

COPY squid.conf /etc/squid/
COPY start-squid.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/start-squid.sh"]
