FROM alpine:latest

ENV CONFIG_JSON=none CERT_PEM=none KEY_PEM=none V2RAY_VERSION=v4.6.4
ENV V2RAY_DOWNLOAD_URL https://github.com/v2ray/v2ray-core/releases/download/${V2RAY_VERSION}/v2ray-linux-64.zip

RUN apk add --no-cache --virtual .build-deps ca-certificates curl \
 && mkdir -m 777 /v2raybin \
 && cd /v2raybin \
 && curl -L -H "Cache-Control: no-cache" -o /v2raybin/v2ray.zip ${V2RAY_DOWNLOAD_URL} \
 && unzip /v2raybin/v2ray.zip  \
 && chmod +x /v2raybin/v2ray \
 && rm -rf v2ray.zip \
 && chgrp -R 0 /v2raybin \
 && chmod -R g+rwX /v2raybin

ADD entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT  /entrypoint.sh

EXPOSE 8080
