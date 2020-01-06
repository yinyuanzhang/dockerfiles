FROM golang:1.7.1-alpine
MAINTAINER abler <mail@xiechaoyi.com>

ADD *.sh /
ADD ./cert /cert
ADD ./ngrok /ngrok
RUN apk add --no-cache git make openssl

ENV DOMAIN wlniao.cn
ENV MY_FILES /wln
ENV HTTP_ADDR 80
ENV HTTPS_ADDR 443
ENV TUNNEL_ADDR 4443

EXPOSE ${HTTP_ADDR}
EXPOSE ${HTTPS_ADDR}
EXPOSE ${TUNNEL_ADDR}

VOLUME ["/wln"]
CMD /bin/sh /start.sh