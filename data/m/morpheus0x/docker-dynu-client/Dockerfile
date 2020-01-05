FROM alpine:3.7
LABEL maintainer="morpheus0x@pm.me"

RUN \
  apk update && \
  apk add --no-cache \
  curl

COPY start.sh /tmp/start.sh
ENTRYPOINT ["/tmp/start.sh"]
