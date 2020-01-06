FROM alpine:latest

LABEL maintainer="Delivery In Box <contato@deliveryinbox.com.br>"

ARG NGINX_VERSION=1.17.1
ARG OPENSSL_BRANCH=master

RUN addgroup -S www
RUN adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G www nginx

# Install dependencies
RUN apk add --no-cache \
      curl \
      pcre \
      libbz2 \
      ca-certificates \
      libressl

RUN apk add --no-cache --virtual .dependencies \
      gcc \
      libc-dev \
      make \
      openssl-dev \
      pcre-dev \
      zlib-dev \
      linux-headers \
      gnupg1 \
      libxslt-dev \
      gd-dev \
      # geoip-dev \
      perl \
      perl-dev \
      # gettext \
      git

# Download OpenSSL
RUN git clone -b $OPENSSL_BRANCH --depth 1 https://github.com/openssl/openssl /srv/openssl
    # cd /srv/openssl && \
    # wget https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/openssl-equal-1.1.1a_ciphers.patch && \
    # patch -p1 < openssl-equal-1.1.1a_ciphers.patch

# Download Brotli
RUN git clone --depth 1 --recurse-submodules https://github.com/google/ngx_brotli.git /tmp/ngx_brotli

# Download nginx
RUN curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o /tmp/nginx.tar.gz
RUN mkdir -p /usr/src
RUN tar -zxC /usr/src -f /tmp/nginx.tar.gz

RUN set -x ; \
    cd /usr/src/nginx-$NGINX_VERSION && \
    ./configure \
      --add-module=/tmp/ngx_brotli \
      --with-openssl=/srv/openssl \
      --with-openssl-opt='enable-tls1_3' \
      --prefix=/etc/nginx \
      --modules-path=/usr/lib/nginx/modules \
      --conf-path=/etc/nginx/nginx.conf \
      --error-log-path=/var/log/nginx/error.log \
      --http-log-path=/var/log/nginx/access.log \
      --http-log-path=/dev/stdout \
      --pid-path=/var/run/nginx.pid \
      --lock-path=/var/run/nginx.lock \
      --http-client-body-temp-path=/var/cache/nginx/client_temp \
      --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
      --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
      --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
      --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
      --sbin-path=/usr/sbin/nginx \
      --user=nginx \
      --group=www \
      # --with-http_dav_module \
      # --with-http_flv_module \
      # --with-http_mp4_module \
      # --with-http_xslt_module=dynamic \
      # --with-http_image_filter_module=dynamic \
      # --with-http_geoip_module=dynamic \
      # --with-stream_geoip_module=dynamic \
      # --with-mail \
      # --with-mail_ssl_module \
      # --with-http_v2_hpack_enc \
      --with-http_v2_module \
      --with-http_ssl_module \
      --with-http_realip_module \
      --with-http_addition_module \
      --with-http_sub_module \
      --with-http_gunzip_module \
      --with-http_gzip_static_module \
      --with-http_random_index_module \
      --with-http_secure_link_module \
      --with-http_stub_status_module \
      --with-http_auth_request_module \
      --with-threads \
      --with-stream \
      --with-stream_ssl_module \
      --with-stream_ssl_preread_module \
      --with-stream_realip_module \
      --with-http_slice_module \
      --with-compat \
      --with-file-aio \
      --with-pcre-jit \
      --with-cc-opt='-g -O2 -fstack-protector-strong -Wformat -Werror=format-security' \
      --with-ld-opt='-Wl,-z,relro -Wl,--as-needed' \
      --without-http_memcached_module \
      --without-mail_pop3_module \
      --without-mail_imap_module \
      --without-mail_smtp_module \
    && \
    make install

    # && apk add --no-cache --virtual .build-deps \
    #     gcc \
    #     libc-dev \
    #     make \
    #     openssl-dev \
    #     pcre-dev \
    #     zlib-dev \
    #     linux-headers \
    #     curl \
    #     gnupg1 \
    #     libxslt-dev \
    #     gd-dev \
    #     geoip-dev \
    #     perl \
    #     perl-dev \
    #     gettext \
    # && curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o nginx.tar.gz \
    #&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o nginx.tar.gz.asc \
    #&& export GNUPGHOME="$(mktemp -d)" \
    #&& found=''; \
    #for server in \
    #    ha.pool.sks-keyservers.net \
    #    hkp://keyserver.ubuntu.com:80 \
    #    hkp://p80.pool.sks-keyservers.net:80 \
    #    pgp.mit.edu \
    #; do \
    #    echo "Fetching GPG key $GPG_KEYS from $server"; \
    #    gpg --keyserver "$server" --keyserver-options timeout=10 --recv-keys "$GPG_KEYS" && found=yes && break; \
    #done; \
    #test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" && exit 1; \
    #gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \
    #&& rm -rf "$GNUPGHOME" nginx.tar.gz.asc \
    # && cd /usr/src/nginx-$NGINX_VERSION \
    # && wget https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/nginx_hpack_push_1.15.3.patch \
    # && patch -p1 < nginx_hpack_push_1.15.3.patch \
    # ; ./configure $CONFIG --with-debug \
    # && make -j$(getconf _NPROCESSORS_ONLN) \
    # && mv objs/nginx objs/nginx-debug \
    # && mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-debug.so \
    # && mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-debug.so \
    # && mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \
    # && mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \
  #   && ./configure $CONFIG \
  #   && make -j$(getconf _NPROCESSORS_ONLN) \
  #   && make install \
  #   && rm -rf /etc/nginx/html/index.html \
  #   && mkdir /etc/nginx/conf.d/ \
  #   && mkdir -p /usr/share/nginx/html/ \
  #   && install -m755 objs/nginx-debug /usr/sbin/nginx-debug \
  #   && install -m755 objs/ngx_http_xslt_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \
  #   && install -m755 objs/ngx_http_image_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \
  #   && install -m755 objs/ngx_http_geoip_module-debug.so /usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \
  #   && install -m755 objs/ngx_stream_geoip_module-debug.so /usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \
  #   && ln -s /usr/lib/nginx/modules /etc/nginx/modules \
  #   && strip /usr/sbin/nginx* \
  #   && strip /usr/lib/nginx/modules/*.so \
  #   # Bring in gettext so we can get `envsubst`, then throw
  #   # the rest away. To do this, we need to install `gettext`
  #   # then move `envsubst` out of the way so `gettext` can
  #   # be deleted completely, then move `envsubst` back.
  #   && apk add --no-cache --virtual .gettext gettext \
  #   && mv /usr/bin/envsubst /tmp/ \
  #   && runDeps="$( \
  #       scanelf --needed --nobanner --format '%n#p' /usr/sbin/nginx /usr/lib/nginx/modules/*.so /tmp/envsubst \
  #           | tr ',' '\n' \
  #           | sort -u \
  #           | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
  #   )" \
  # && apk add --no-cache --virtual .nginxdeps $runDeps \
  # && mv /tmp/envsubst /usr/local/bin/
  
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# Bring in tzdata so users could set the timezones through the environment
# variables
RUN apk add --no-cache tzdata

# Nginx bad blocker
RUN mkdir /usr/local/sbin
RUN wget https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/master/install-ngxblocker -O /usr/local/sbin/install-ngxblocker
RUN chmod +x /usr/local/sbin/install-ngxblocker
RUN /usr/local/sbin/install-ngxblocker -x
RUN chmod +x /usr/local/sbin/setup-ngxblocker
RUN chmod +x /usr/local/sbin/update-ngxblocker
RUN /usr/local/sbin/setup-ngxblocker -x -e conf -v /etc/nginx/sites-available
COPY ./update-ngxblocker /etc/periodic/hourly/update-ngxblocker
RUN chmod a+x /etc/periodic/hourly/update-ngxblocker

# Remove dependencies
# RUN apk del --no-cache .gettext
RUN apk del --no-cache .dependencies
RUN rm -rf /tmp/*
RUN rm -rf /srv/openssl
RUN rm -rf /usr/src/nginx-$NGINX_VERSION

EXPOSE 80 443

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]