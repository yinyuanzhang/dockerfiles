FROM alpine:edge
MAINTAINER otofu <otofu.xxx+docker@gmail.com>

RUN apk --update add --no-cache dnsmasq \
 && rm -rf /var/cache/apk/*

EXPOSE 53 53/udp

ENTRYPOINT ["dnsmasq", "-k" ]
