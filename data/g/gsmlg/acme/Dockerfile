FROM alpine:3.8

MAINTAINER GSMLG < me@gsmlg.org >

RUN apk update \
    && apk add curl \
    && apk add openssl \
    && mkdir -p /acme \
    && mkdir -p /acme/dnsapi \
    && mkdir -p /certs \
    && curl -fsSL --compressed https://raw.githubusercontent.com/Neilpang/acme.sh/master/acme.sh -o /acme.sh \
    && sh /acme.sh --install --home /acme --config-home /acme --certhome /certs --accountconf /acme/account.conf --accountemail "acme@gsmlg.org" \
    && curl -fsSL --compressed https://raw.githubusercontent.com/Neilpang/acme.sh/master/dnsapi/dns_cf.sh -o /acme/dnsapi/dns_cf.sh \
    && rm -f /acme.sh \
    && rm -rf /var/cache/apk/*

ENV CF_Email=me@gsmlg.org \
    CF_Key=

COPY entrypoint.sh domains.txt /

ENTRYPOINT ["/entrypoint.sh"]
