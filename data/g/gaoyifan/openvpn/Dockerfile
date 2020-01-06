FROM smartentry/centos:7-0.3.7

MAINTAINER Yifan Gao <git@yfgao.com>

EXPOSE 1194/tcp 1194/udp

VOLUME /etc/openvpn

CMD ["/usr/sbin/openvpn", "--cd", "/etc/openvpn/", "--config", "server.conf"]

ADD . $ASSETS_DIR

RUN smartentry.sh build

