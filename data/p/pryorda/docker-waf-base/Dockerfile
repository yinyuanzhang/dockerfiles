FROM ubuntu:18.04

ENV NGINX_VERSION=1.15.11

ADD http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz /

RUN tar -xvf /nginx-${NGINX_VERSION}.tar.gz && \
      apt-get update && \
      apt-get install -y git libyajl-dev build-essential libpcre3 libpcre3-dev libssl-dev libtool autoconf apache2-dev libxml2-dev libcurl4-openssl-dev automake pkgconf && \
      cd /usr/src/ && \
      git clone -b nginx_refactoring https://github.com/SpiderLabs/ModSecurity.git /usr/src/modsecurity && \
      cd /usr/src/modsecurity && \
      ./autogen.sh && \
      ./configure --enable-standalone-module --with-yajl --disable-mlogc && \
      make && \
      cd /nginx-${NGINX_VERSION} && \
      adduser --disabled-password --system --home /var/cache/nginx --shell /sbin/nologin --group nginx && \
      ./configure --user=nginx --group=nginx --with-debug --with-ipv6 --with-http_ssl_module --add-module=/usr/src/modsecurity/nginx/modsecurity --with-http_ssl_module --without-http_access_module --without-http_auth_basic_module --without-http_autoindex_module --without-http_empty_gif_module --without-http_fastcgi_module --without-http_referer_module --without-http_memcached_module --without-http_scgi_module --without-http_split_clients_module --without-http_ssi_module --without-http_uwsgi_module && \
      make && \
      make install
