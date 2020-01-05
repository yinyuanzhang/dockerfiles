FROM alpine:3.9

ENV JQ_VERSION=1.6-r0

RUN apk add --no-cache jq=$JQ_VERSION

CMD ["/usr/bin/jq", "--help"]

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.name="jq" \
      org.label-schema.version="1.6-r0" \
      org.label-schema.url="https://stedolan.github.io/jq/" \
      org.label-schema.vcs-url="https://github.com/oildex/docker-jq"
