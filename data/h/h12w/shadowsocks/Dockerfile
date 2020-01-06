FROM debian:latest
MAINTAINER Hǎiliàng Wáng <w@h12.me>

ENV VER 1.1.4
ENV BIN /usr/local/bin
LABEL version=$VER

ADD http://dl.chenyufei.info/shadowsocks/$VER/shadowsocks-server-linux64-$VER.gz $BIN/ss-server.gz
RUN gunzip   $BIN/ss-server.gz
RUN chmod +x $BIN/ss-server

ENTRYPOINT ["ss-server"]
