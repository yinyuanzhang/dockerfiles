FROM openresty/openresty:alpine-fat
LABEL maintainer="Xuxing Huang augustushwang@gmail.com"

RUN apk add --no-cache --virtual .run-deps openssl-dev 
RUN luarocks install lua-resty-openidc

ENTRYPOINT ["/usr/local/openresty/nginx/sbin/nginx", "-g", "daemon off;"]
