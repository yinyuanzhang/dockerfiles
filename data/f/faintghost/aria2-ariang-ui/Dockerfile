FROM alpine:edge
LABEL maintainer="zhang.yaowei@live.com"

ENV ARIANG_VERSION 1.1.4

RUN apk update \
    && apk add --no-cache --update bash \
	&& mkdir -p /conf \
	&& mkdir -p /conf-copy \
	&& mkdir -p /data \
    && apk add --no-cache --update aria2 \
    && mkdir -p /aria2ng \
    && cd /aria2ng \
	&& apk add --no-cache --update wget \
	&& wget -N --no-check-certificate https://github.com/mayswind/AriaNg/releases/download/${ARIANG_VERSION}/AriaNg-${ARIANG_VERSION}.zip && unzip AriaNg-${ARIANG_VERSION}.zip && rm -rf AriaNg-${ARIANG_VERSION}.zip \
	&& apk del wget \
	&& apk add --update darkhttpd

ADD files/start.sh /conf-copy/start.sh
ADD files/aria2.conf /conf-copy/aria2.conf
ADD files/on-complete.sh /conf-copy/on-complete.sh

RUN chmod +x /conf-copy/start.sh

WORKDIR /
VOLUME ["/data"]
VOLUME ["/conf"]

ENV RPC_SECRET=""

EXPOSE 6800
EXPOSE 80

CMD ["/conf-copy/start.sh"]