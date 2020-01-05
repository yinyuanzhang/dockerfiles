FROM alpine:latest
MAINTAINER Andreas Oeldemann <hey@aoel.io>

RUN apk add --update dhcp \
 && touch /var/lib/dhcp/dhcpd.leases \
 && rm -rf /var/cache/apk/*

VOLUME ["/config"]

EXPOSE 67/tcp

ENTRYPOINT ["dhcpd", "-d", "-cf", "/config/dhcpd.conf"]
