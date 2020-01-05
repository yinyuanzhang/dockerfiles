FROM alpine:latest
MAINTAINER Abi X Renhart <arenhart@avvo.com>

RUN apk add --no-cache --update \
    curl \
    bash

ADD opt /opt
ENTRYPOINT ["/opt/rancher/scripts/entrypoint.sh"]