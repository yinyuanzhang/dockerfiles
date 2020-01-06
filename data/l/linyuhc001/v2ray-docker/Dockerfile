FROM alpine:3.6

ENV TZ 'Asia/Shanghai'
ENV V2RAY_VERSION v2.34 

WORKDIR /root

RUN apk upgrade --update \
    && apk add \
        bash \
        tzdata \
        curl \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && mkdir -p \ 
        /var/log/v2ray \
        /tmp/v2ray \
        /etc/v2ray/ \
    && curl -L -H "Cache-Control: no-cache" -o /tmp/v2ray/v2ray.zip \
        https://github.com/v2ray/v2ray-core/releases/download/${V2RAY_VERSION}/v2ray-linux-64.zip \
    && unzip /tmp/v2ray/v2ray.zip -d /tmp/v2ray/ \
    && cp /tmp/v2ray/v2ray-${V2RAY_VERSION}-linux-64/v2ray /usr/local/bin/v2ray \
    && chmod +x /usr/local/bin/v2ray \
    && apk del curl \
    && rm -rf /tmp/v2ray \
    && rm -rf /var/cache/apk/*

ADD entrypoint.sh /entrypoint.sh
ADD config.json /etc/v2ray/config.json
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
