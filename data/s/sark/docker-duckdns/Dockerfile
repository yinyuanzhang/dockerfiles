FROM alpine:latest
RUN apk add --update curl jq && rm -rf /var/cache/apk/*
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
