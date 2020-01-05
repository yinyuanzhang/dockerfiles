FROM alpine:latest

#ENV CONFIG_JSON=none CERT_PEM=none KEY_PEM=none VER=3.46
ENV CONFIG_JSON=none CERT_PEM=none KEY_PEM=none VER=4.9.0

RUN apk add --no-cache --virtual .build-deps ca-certificates curl \
 && mkdir -m 777 /v2raybin \ 
 && mkdir -m 777 /v2raytmp_111 \
 #&& cd /v2raybin \
 && cd /v2raytmp_111 \
 && curl -L -H "Cache-Control: no-cache" -o v2ray.zip https://github.com/v2ray/v2ray-core/releases/download/v$VER/v2ray-linux-64.zip \
 && unzip v2ray.zip \
 #&& mv /v2raybin/v2ray-v$VER-linux-64/v2ray /v2raybin/ \
 && mv /v2raytmp_111/v2ray /v2raybin/ \
 #&& mv /v2raybin/v2ray-v$VER-linux-64/v2ctl /v2raybin/ \
 && mv /v2raytmp_111/v2ctl /v2raybin/ \
 #&& mv /v2raybin/v2ray-v$VER-linux-64/geoip.dat /v2raybin/ \
 && mv /v2raytmp_111/geoip.dat /v2raybin/ \
 #&& mv /v2raybin/v2ray-v$VER-linux-64/geosite.dat /v2raybin/ \
 && mv /v2raytmp_111/geosite.dat /v2raybin/ \
 && chmod +x /v2raybin/v2ray \
 && chmod +x /v2raybin/v2ctl \
 && rm -rf v2ray.zip \
 #&& rm -rf v2ray-v$VER-linux-64 \
 && cd /v2raybin \
 && rm -rf /v2raytmp_111 \
 && chgrp -R 0 /v2raybin \
 && chmod -R g+rwX /v2raybin 
 
ADD entrypoint.sh /entrypoint.sh
ADD config.json /v2raybin/config.json

RUN chmod +x /entrypoint.sh 

ENTRYPOINT  /entrypoint.sh 

EXPOSE 8080
