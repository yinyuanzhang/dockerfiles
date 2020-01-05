FROM alpine:3.10.2
MAINTAINER developers@khipu.com

ARG GOSU_VERSION=1.11
ARG KHIPU_GID=2000
ARG KHIPU_UID=2000

RUN apk update \
    && apk upgrade \
    && apk add --update curl bash gettext su-exec \
    && rm -rf /var/cache/apk/*

RUN adduser -u ${KHIPU_UID} -D -H khipu \
    && mkdir -p /opt/khipu \
    && cd /opt/khipu \
    && mkdir bin etc share log var \
    && chown -R khipu:khipu /opt/khipu

RUN curl -o /usr/local/bin/gosu -fsSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 \
    && chmod +x /usr/local/bin/gosu
