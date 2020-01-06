FROM lsiobase/alpine:amd64-3.10
EXPOSE 53 53/udp
VOLUME /config
COPY s6/ /
RUN \
  apk add --no-cache \
    dnsmasq
