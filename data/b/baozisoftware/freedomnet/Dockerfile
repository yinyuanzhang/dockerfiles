#Base image
FROM ubuntu:16.04
MAINTAINER Baozisoftware Diklic "https://github.com/Baozisoftware"

ENV SSVERION 0.0.11
ENV SSPORT 12345
ENV SSM AEAD_CHACHA20_POLY1305
ENV SSKEY 12345678

#Install Shadowsocks
ADD https://github.com/shadowsocks/go-shadowsocks2/releases/download/v$SSVERION/shadowsocks2-linux.gz /
RUN gunzip shadowsocks2-linux.gz
RUN chmod +x /shadowsocks2-linux

#Other
EXPOSE $SSPORT
CMD /shadowsocks2-linux -s "ss://$SSM:$SSKEY@:$SSPORT"
