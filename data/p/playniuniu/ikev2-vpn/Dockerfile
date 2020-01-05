FROM alpine:latest
MAINTAINER playniuniu@gmail.com

# Install strongswan
RUN apk --no-cache --update add curl openssl strongswan \
    && rm -r /var/cache/apk/*

# Strongswan Configuration
ADD ./config/ipsec.conf /etc/ipsec.conf
ADD ./config/strongswan.conf /etc/strongswan.conf
ADD startvpn.sh /usr/bin/startvpn

VOLUME /www
ADD web /www

EXPOSE 80 500/udp 4500/udp

ENTRYPOINT ["/usr/bin/startvpn"]
