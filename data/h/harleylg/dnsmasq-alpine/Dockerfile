FROM alpine

RUN apk --no-cache add dnsmasq

EXPOSE 53 53/udp

VOLUME [ "/etc/dnsmasq" ]

ENTRYPOINT ["dnsmasq", "-k", "-c /etc/dnsmasq/dnsmasq.conf"]