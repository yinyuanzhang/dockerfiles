FROM jalaziz/base:alpine

ENV NGINX_VERSION 1.9.13
ENV NGINX_RTMP_VERSION 1.1.7
ENV NGINX_DEVEL_KIT_VERSION 0.2.19
ENV NGINX_LUA_VERSION 0.10.2

RUN  apk add --update build-base pcre-dev openssl-dev zlib-dev luajit-dev linux-headers \
  && mkdir -p /tmp/src \
  && cd /tmp/src \
  && wget -qO- http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar -xz \
  && wget -qO- https://github.com/arut/nginx-rtmp-module/archive/v${NGINX_RTMP_VERSION}.tar.gz | tar -xz \
  && wget -qO- https://github.com/simpl/ngx_devel_kit/archive/v${NGINX_DEVEL_KIT_VERSION}.tar.gz | tar -xz \
  && wget -qO- https://github.com/openresty/lua-nginx-module/archive/v${NGINX_LUA_VERSION}.tar.gz| tar -xz \
  && cd nginx-${NGINX_VERSION} \
  && ./configure --prefix=/usr/share/nginx \
    --sbin-path=/usr/sbin/nginx \
    --conf-path=/etc/nginx/nginx.conf \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/run/nginx.lock \
    --error-log-path=/var/log/nginx/error.log \
    --http-log-path=/var/log/nginx/access.log \
    --http-client-body-temp-path=/var/lib/nginx/tmp/client_body \
    --http-proxy-temp-path=/var/lib/nginx/tmp/proxy \
    --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi \
    --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi \
    --http-scgi-temp-path=/var/lib/nginx/tmp/scgi \
    --user=nginx \
    --group=nginx \
    --with-ipv6 \
    --with-file-aio \
    --with-pcre-jit \
    --with-http_dav_module \
    --with-http_ssl_module \
    --with-http_stub_status_module \
    --with-http_gzip_static_module \
    --with-http_v2_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_sub_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_auth_request_module \
    --with-threads \
    --with-stream \
    --with-stream_ssl_module \
    --with-mail \
    --with-mail_ssl_module \
    --add-module=/tmp/src/nginx-rtmp-module-${NGINX_RTMP_VERSION} \
    --add-module=/tmp/src/ngx_devel_kit-${NGINX_DEVEL_KIT_VERSION} \
    --add-module=/tmp/src/lua-nginx-module-${NGINX_LUA_VERSION} \
  && make \
  && make install \
  && cp /tmp/src/nginx-rtmp-module-${NGINX_RTMP_VERSION}/stat.xsl /usr/share/nginx/html/ \
  && apk del build-base \
  && rm -rf /var/cache/apk/* /tmp/*

RUN addgroup -S nginx \
  && addgroup -S www-data || true \
  && adduser -S -G nginx -H -h /var/www/localhost/htdocs -s /sbin/nologin -D nginx \
  && addgroup nginx www-data \
  && chmod 700 /var/log/nginx \
  && touch /var/log/nginx/access.log \
  && chmod 640 /var/log/nginx/access.log \
  && touch /var/log/nginx/error.log \
  && chmod 640 /var/log/nginx/error.log \
  && chown -R nginx:nginx /var/log/nginx \
  && mkdir -p -m 700 /var/lib/nginx \
  && mkdir -p -m 700 /var/lib/nginx/tmp \
  && chown -R nginx:nginx /var/lib/nginx \
  && mkdir -p -m 755 /etc/nginx/conf.d

# forward request and error logs to docker log collector
RUN  ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

# commented out since it shouldn't be shared by everyone
# RUN openssl dhparam -out /etc/nginx/dhparams.pem 2048

COPY conf /etc/nginx

VOLUME ["/var/cache/nginx", "/etc/nginx/conf.d"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
