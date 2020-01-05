FROM alpine:latest
MAINTAINER Cameron Meindl <cmeindl@gmail.com>

RUN set -xe && \
    apk add --no-cache dnsmasq && \

    # Set
    echo "conf-dir=/etc/dnsmasq.d/" >> /etc/dnsmasq.conf && \
    echo "no-negcache" >> /etc/dnsmasq.conf && \
    echo "local-ttl=300" >> /etc/dnsmasq.conf && \
    echo "no-poll" >> /etc/dnsmasq.conf && \
    echo "cache-size=10000" >> /etc/dnsmasq.conf

VOLUME ["/etc/dnsmasq.d"]
VOLUME ["/var/lib/tftpboot"]
VOLUME ["/var/lib/dnsmasq"]

CMD ["dnsmasq", "--no-daemon", "--user=dnsmasq", "--group=dnsmasq"]
