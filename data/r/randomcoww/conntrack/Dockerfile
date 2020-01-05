FROM alpine:edge

RUN set -x \
  \
  && apk add --no-cache \
    conntrack-tools

ENTRYPOINT ["/usr/sbin/conntrackd"]
