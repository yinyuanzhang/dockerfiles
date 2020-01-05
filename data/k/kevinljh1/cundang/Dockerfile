FROM alpine:latest

ENV CONFIG_JSON=none CERT_PEM=none KEY_PEM=none VER=3.36

RUN apk add --no-cache --virtual .build-deps ca-certificates curl wget python nodejs npm unzip \
 && mkdir -m 777 /v2raybin \ 
 && mkdir -m 777 /ssjs \
 && cd /v2raybin \
 && curl -L -H "Cache-Control: no-cache" -o v2ray.zip https://github.com/v2ray/v2ray-core/releases/download/v$VER/v2ray-linux-64.zip \
 && unzip v2ray.zip \
 && mv /v2raybin/v2ray-v$VER-linux-64/v2ray /v2raybin/ \
 && mv /v2raybin/v2ray-v$VER-linux-64/v2ctl /v2raybin/ \
 && mv /v2raybin/v2ray-v$VER-linux-64/geoip.dat /v2raybin/ \
 && mv /v2raybin/v2ray-v$VER-linux-64/geosite.dat /v2raybin/ \
 && chmod +x /v2raybin/v2ray \
 && rm -rf v2ray.zip \
 && rm -rf v2ray-v$VER-linux-64 \
 && chgrp -R 0 /v2raybin \
 && chmod -R g+rwX /v2raybin \
 && cd /ssjs \
 && wget https://github.com/kevinljh11/shadowsocks-openshift/archive/master.zip \
 && unzip master.zip \
 && mv shadowsocks-openshift-master osjs \
 && cd osjs \
 && wget https://github.com/keviljh3/shadowsocks-openshift/raw/master/server_linux_amd64 \
 && wget https://github.com/keviljh3/shadowsocks-openshift/raw/master/udp2raw_amd64 \
 && chmod +x server_linux_amd64 \
 && chmod +x udp2raw_amd64 \
 && chmod 777 config.json \
 && npm install
 
ADD entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh 

ENTRYPOINT  /entrypoint.sh 

EXPOSE 8080
EXPOSE 8081
