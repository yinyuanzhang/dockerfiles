ARG OPENRESTY_VERSION=1.15.8.2

FROM openresty/openresty:${OPENRESTY_VERSION}-alpine-fat

RUN apk add --no-cache nginx-mod-http-lua

COPY etc /etc/

EXPOSE 80
EXPOSE 9145