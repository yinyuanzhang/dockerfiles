FROM alpine:latest
RUN apk add --update curl && rm -rf /var/cache/apk/*
COPY entrypoint.sh /
COPY cacert_root_256.crt /usr/local/share/ca-certificates
RUN update-ca-certificates
ENTRYPOINT ["/entrypoint.sh"]
CMD ["curl"]