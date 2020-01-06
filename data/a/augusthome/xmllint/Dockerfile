FROM alpine:3.10
RUN apk add --update \
    libxml2-utils

WORKDIR /data
VOLUME ["/data"]

ENTRYPOINT ["xmllint"]
CMD ["--help"]