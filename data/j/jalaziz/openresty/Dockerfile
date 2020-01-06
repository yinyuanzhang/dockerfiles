FROM jalaziz/base:alpine

ENV OPENRESTY_VERSION 1.9.7.4
ENV NGINX_RTMP_VERSION 1.1.7
ENV LUAROCKS_VERSION 2.3.0

RUN  apk add --update build-base perl pcre-dev openssl-dev zlib-dev \
     ncurses-dev readline-dev linux-headers \
  && mkdir -p /tmp/src \
  && cd /tmp/src \
  && wget -qO- https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz | tar -xz \
  && wget -qO- https://github.com/arut/nginx-rtmp-module/archive/v${NGINX_RTMP_VERSION}.tar.gz | tar -xz \
  && wget -qO- http://keplerproject.github.io/luarocks/releases/luarocks-${LUAROCKS_VERSION}.tar.gz | tar -xz \
  && cd openresty-${OPENRESTY_VERSION} \
  && ./configure --prefix=/usr/share/openresty \
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
  && make build \
  && make install \
  && cp /tmp/src/nginx-rtmp-module-${NGINX_RTMP_VERSION}/stat.xsl /usr/share/openresty/nginx/html/ \
  && cd ../luarocks-${LUAROCKS_VERSION} \
  && ./configure --prefix=/usr/share/openresty/luajit \
    --with-lua=/usr/share/openresty/luajit/ \
    --lua-suffix=jit \
    --with-lua-include=/usr/share/openresty/luajit/include/luajit-2.1 \
  && make build \
  && make install \
  && /usr/share/openresty/luajit/bin/luarocks install lua-resty-template \
  && apk del build-base \
  && rm -rf /var/cache/apk/* /tmp/* ~/.cache

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

COPY conf /etc/nginx

VOLUME ["/var/cache/nginx", "/etc/nginx/conf.d"]

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
