FROM exira/base:3.4.2

MAINTAINER exira.com <info@exira.com>

ENV NGINX_VERSION=1.11.3 \
    NGX_CACHE_PURGE_VERSION=2.3 \
    HEADERS_MORE_VERSION=0.30

RUN \
    # Install build and runtime packages
    build_pkgs="build-base linux-headers openssl-dev pcre-dev wget zlib-dev" && \
    runtime_pkgs="ca-certificates openssl pcre zlib" && \
    apk update && \
    apk upgrade && \
    apk --update --no-cache add ${build_pkgs} ${runtime_pkgs} && \
    update-ca-certificates && \

    # download unpack nginx-src
    mkdir /tmp/nginx && \
    cd /tmp/nginx && \
    wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \
    tar xzf nginx-${NGINX_VERSION}.tar.gz && \
    cd nginx-${NGINX_VERSION} && \

    wget https://github.com/FRiCKLE/ngx_cache_purge/archive/${NGX_CACHE_PURGE_VERSION}.tar.gz && \
    tar xzf ${NGX_CACHE_PURGE_VERSION}.tar.gz && \

    wget https://github.com/openresty/headers-more-nginx-module/archive/v${HEADERS_MORE_VERSION}.tar.gz && \
    tar xzf v${HEADERS_MORE_VERSION}.tar.gz

RUN \
    #compile
    cd /tmp/nginx/nginx-${NGINX_VERSION} && \
    ./configure \
        --prefix=/usr/share/nginx \
        --sbin-path=/usr/sbin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/run/nginx.lock \
        --http-client-body-temp-path=/var/cache/nginx/client_temp \
        --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
        --user=www-data \
        --group=www-data \

        --with-file-aio \
        --with-ipv6 \
        --with-threads \

        --with-http_gzip_static_module \
        --with-http_gunzip_module \
        --with-http_ssl_module \
        --with-http_stub_status_module \
        --with-http_v2_module \

        --without-http_autoindex_module \
        --without-http_browser_module \
        --without-http_empty_gif_module \
        --without-http_geo_module \
        --without-http_memcached_module \
        --without-http_scgi_module \
        --without-http_split_clients_module \
        --without-http_ssi_module \
        --without-http_uwsgi_module \

        --add-module=./ngx_cache_purge-${NGX_CACHE_PURGE_VERSION} \
        --add-module=./headers-more-nginx-module-${HEADERS_MORE_VERSION} && \
    make && \
    make install && \
    make clean

RUN \
    # strip debug symbols from the binary (GREATLY reduces binary size)
    strip -s /usr/sbin/nginx && \

    # patch out server name
    sed -i 's/nginx\r/exira\r/' /usr/sbin/nginx && \

    # add www-data user
    mkdir -p /home/www-data && \
    addgroup -g 433 -S www-data && \
    adduser -u 431 -S -D -G www-data -h /home/www-data -s /sbin/nologin www-data && \
    chown -R www-data:www-data /home/www-data && \

    # create cache dir
    mkdir /var/cache/nginx && \

    # remove NGINX dev dependencies
    apk del ${build_pkgs} && \

    # other clean up
    cd / && \
    rm /etc/nginx/*.default && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf /var/www/*

ADD root /

RUN chown -R www-data:www-data /var/www

WORKDIR /var/www/

VOLUME /var/cache/nginx

EXPOSE 80 443
