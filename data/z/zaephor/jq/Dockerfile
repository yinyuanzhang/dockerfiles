FROM alpine:3.8
RUN apk --no-cache add ca-certificates git jq bash curl && \
  rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/jq"]
