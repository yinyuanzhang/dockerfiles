FROM alpine:edge

RUN set -x \
  \
  && apk add --no-cache \
    nftables

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
