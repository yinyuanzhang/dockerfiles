FROM alpine:3.6
MAINTAINER SFoxDev <admin@sfoxdev.com>

ENV LANG="en_US.UTF-8" \
    SOFTETHER_VERSION="v4.22-9634-beta"

ADD scripts/ /
RUN set -ex ; \
    addgroup -S softether ; adduser -D -H softether -g softether -G softether -s /sbin/nologin ; \
    apk add --no-cache --virtual .build-deps gcc make musl-dev ncurses-dev openssl-dev readline-dev wget ; \
    chmod +x /entrypoint.sh ; \

    wget --no-check-certificate -O - https://github.com/SoftEtherVPN/SoftEtherVPN/archive/${SOFTETHER_VERSION}.tar.gz | tar xzf - ; \
    cd SoftEtherVPN-${SOFTETHER_VERSION:1} ; \

    for file in /patchs/*.sh; do /bin/sh "$file"; done ; \
    cp src/makefiles/linux_64bit.mak Makefile ; \
    make ; make install ; make clean ; \

    strip /usr/vpnserver/vpnserver ; \
    mkdir -p /etc/vpnserver /var/log/vpnserver; ln -s /etc/vpnserver/vpn_server.config /usr/vpnserver/vpn_server.config ; \
    mkdir -p /var/log/vpnserver/server_log; ln -s /var/log/vpnserver/server_log /usr/vpnserver/server_log ; \
    mkdir -p /var/log/vpnserver/security_log; ln -s /var/log/vpnserver/security_log /usr/vpnserver/security_log ; \
    mkdir -p /var/log/vpnserver/packet_log; ln -s /var/log/vpnserver/packet_log /usr/vpnserver/packet_log ; \
    chown -R softether:softether /usr/vpnserver ; \

    apk del .build-deps ; \
    apk add --no-cache --virtual .run-deps libcap libcrypto1.0 libssl1.0 ncurses-libs readline su-exec ; \
    setcap 'cap_net_bind_service=+ep' /usr/vpnserver/vpnserver ; \

    cd .. ; \
    rm -rf /usr/vpnbridge /usr/bin/vpnbridge /usr/vpnclient /usr/bin/vpnclient /usr/vpncmd /usr/bin/vpncmd /usr/bin/vpnserver \
           /patchs SoftEtherVPN-${SOFTETHER_VERSION:1} /var/cache/apk/* /tmp/* ;

EXPOSE 443/tcp 992/tcp 1194/udp 5555/tcp

VOLUME ["/etc/vpnserver", "/var/log/vpnserver"]

USER root
CMD ["/usr/vpnserver/vpnserver", "execsvc"]
