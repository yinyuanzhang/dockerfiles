FROM alpine:3.8

LABEL maintainer='Hugo Fonseca <https://github.com/hugomcfonseca>'

WORKDIR /app

RUN apk --update add --no-cache --virtual .deps \
        curl \
    && apk --update add --no-cache \
        git \
    && curl -sSLo /tmp/ghr.tar.gz https://github.com/tcnksm/ghr/releases/download/v0.12.0/ghr_v0.12.0_linux_amd64.tar.gz \
    && tar xfz /tmp/ghr.tar.gz -C /tmp \
    && mv /tmp/ghr_v0.12.0_linux_amd64/ghr /usr/local/bin \
    && apk del .deps \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apk/lists/* 

ENTRYPOINT ["ghr"]
