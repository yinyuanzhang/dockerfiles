FROM debian:buster-slim

LABEL maintainer="Normunds Galejs normisg@gmail.com"

ENV NGINX_VERSION 1.17.4
ENV PCRE_VERSION 8.43
ENV ZLIB_VERSION 1.2.11
ENV OPENSSL_VERSION 1.1.1d
ENV NGX_HEADERS_MORE 0.33

# https://www.nginx.com/resources/library/modsecurity-3-nginx-quick-start-guide
RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-utils \
        autoconf \
        automake \
        build-essential \
        ca-certificates \
        curl \
        git \
        libcurl4-openssl-dev \
        libgeoip-dev \
        liblmdb-dev \
        libpcre++-dev \
        libtool \
        libxml2-dev \
        libyajl-dev \
        pkgconf \
        wget \
        zlib1g-dev && \
    mkdir -p /install && \
    cd /install && \
    git clone --depth 1 -b v3/master --single-branch https://github.com/SpiderLabs/ModSecurity && \
    cd ModSecurity && \
    git submodule init && \
    git submodule update && \
    ./build.sh && \
    ./configure && \
    make && \
    make install && \
    cd /install && \
    git clone --depth 1 https://github.com/SpiderLabs/ModSecurity-nginx.git && \
    wget -qO- https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar zxv && \
    wget -qO- https://github.com/openresty/headers-more-nginx-module/archive/v${NGX_HEADERS_MORE}.tar.gz | tar zxv && \
    wget -qO- https://ftp.pcre.org/pub/pcre/pcre-${PCRE_VERSION}.tar.gz | tar zxv && \
    wget -qO- http://www.zlib.net/zlib-${ZLIB_VERSION}.tar.gz | tar zxv && \
    wget -qO- https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz | tar zxv && \
    cd nginx-${NGINX_VERSION} && \
    ./configure \
        --prefix=/usr/share/nginx \
        --sbin-path=/usr/sbin/nginx \
        --modules-path=/usr/lib/nginx/modules \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/lock/nginx.lock \
        --user=www-data \
        --group=www-data \
        --http-client-body-temp-path=/var/cache/nginx/client_temp \
        --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
        --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
        --without-http_uwsgi_module \
        --without-mail_pop3_module \
        --without-mail_imap_module \
        --without-mail_smtp_module \
        --with-debug \
        --with-file-aio \
        --with-threads \
        --with-http_addition_module \
        --with-http_auth_request_module \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_mp4_module \
        --with-http_random_index_module \
        --with-http_realip_module \
        --with-http_secure_link_module \
        --with-http_slice_module \
        --with-http_stub_status_module \
        --with-http_sub_module \
        --with-http_v2_module \
        --with-stream \
        --with-stream_realip_module \
        --with-stream_ssl_module \
        --with-stream_ssl_preread_module \
        --with-openssl=../openssl-${OPENSSL_VERSION} \
        --with-openssl-opt=enable-ec_nistp_64_gcc_128 \
        --with-openssl-opt=no-nextprotoneg \
        --with-openssl-opt=no-weak-ssl-ciphers \
        --with-openssl-opt=no-ssl3 \
        --with-pcre=../pcre-${PCRE_VERSION} \
        --with-pcre-jit \
        --with-zlib=../zlib-${ZLIB_VERSION} \
        --add-module=../ModSecurity-nginx \
        --add-module=../headers-more-nginx-module-${NGX_HEADERS_MORE} \
        --with-cc-opt='-g -O2 -fPIE -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2' \
        --with-ld-opt='-Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-z,now' && \
    make && \
    make install && \
    rm -rf /install && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    openssl dhparam 2048 > /etc/nginx/dhparam && \
    apt-get -y remove apt-utils \
        autoconf \
        automake \
        build-essential \
        curl \
        git \
        libpcre++-dev \
        libtool \
        pkgconf \
        wget \
        zlib1g-dev && \
    rm -rf /install && \
    mkdir -p /var/cache/nginx && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

COPY ./nginx /etc/nginx

EXPOSE 80

EXPOSE 443

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]    
