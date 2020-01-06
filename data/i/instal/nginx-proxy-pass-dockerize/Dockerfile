FROM nginx:1.13-alpine
ENV TERM xterm-256color
ENV LUA_VERSION 5.1
ENV LUA_PACKAGE lua${LUA_VERSION}
ENV LUAROCKS_VERSION 3.0.3

RUN apk update && apk add \
    python2 \
    py2-pip \
    wrk \
    curl \
    nano \
    nginx-mod-http-lua \
    ${LUA_PACKAGE} \
    ${LUA_PACKAGE}-dev \
    luarocks \
    zlib-dev \
    build-base


RUN ls /usr/bin/luarocks*
RUN ln -s /usr/bin/luarocks-${LUA_VERSION} /usr/bin/luarocks
RUN luarocks install lua-zlib


RUN pip install --upgrade pip \
    && pip install \
        Jinja2 \
    && rm -r /root/.cache

COPY nginx.template.conf /app/nginx.template.conf
COPY inflate_body.lua /var/lib/nginx/inflate_body.lua
COPY start.sh /app/start.sh
COPY environment_template.py /app/environment_template.py

RUN chmod 700 /app/start.sh

ENV DEBIAN_FRONTEND noninteractive

ENV WORKDIR /app

# these are the main two parameters
ENV NGINX_SERVER_PORT '8080'
ENV NGINX_UPSTREAM_SERVER '127.0.0.1:8000'

ENV NGINX_ERROR_LOGLEVEL 'info'
ENV NGINX_MULTI_ACCEPT 'on'
ENV NGINX_WORKER_PROCESSES '4'
ENV NGINX_WORKER_CONNECTIONS '4096'
ENV NGINX_CLIENT_MAX_BODY_SIZE '70M'
ENV NGINX_CLIENT_BODY_TIMEOUT '60s'
ENV NGINX_FASTCGI_READ_TIMEOUT '60s'
ENV NGINX_PROXY_READ_TIMEOUT '60s'
ENV NGINX_GZIP_TYPES 'application/xml application/json'
ENV NGINX_UPSTREAM_KEEPALIVE '32'
ENV NGINX_KEEPALIVE_TIMEOUT '3600s'
ENV NGINX_KEEPALIVE_REQUESTS '9999999'
ENV NGINX_HEALTHCHECK_PATH '/__healthcheck'
ENV NGINX_ACCESS_LOG_TO_STDOUT 'true'
ENV NGINX_INFLATE_COMPRESSED_BODY 'false'
ENV LUA_PATH=/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua;/usr/local/lib/lua/5.1/?.lua;/usr/local/lib/lua/5.1/?/init.lua;/usr/share/lua/5.1/?.lua;/usr/share/lua/5.1/?/init.lua;/usr/lib/lua/5.1/?.lua;/usr/lib/lua/5.1/?/init.lua;/usr/share/lua/common/?.lua;/usr/share/lua/common/?/init.lua;./?.lua;./?/init.lua
ENV LUA_CPATH=/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so;/usr/lib/lua/5.1/?.so;/usr/lib/lua/5.1/loadall.so;./?.so

WORKDIR $WORKDIR

EXPOSE 8080

CMD ["/app/start.sh"]
