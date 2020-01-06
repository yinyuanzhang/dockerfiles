FROM alpine

ADD ./entrypoint.sh /entrypoint.sh
RUN apk --no-cache add wget openssl ca-certificates

ENTRYPOINT ["/entrypoint.sh"]
