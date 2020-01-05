FROM nginx:1.16.0-alpine 

LABEL maintainer="coolbaby"

RUN apk add --no-cache --virtual .build-deps \
	gcc \
	libc-dev \
	make \
	openssl-dev \
	pcre-dev \
	zlib-dev \
	linux-headers \
	curl \
	wget \
	gnupg1 \
	libxslt-dev \
	gd-dev \
	geoip-dev \
    unzip \
&& mkdir -p /usr/src && cd /usr/src \
&& wget https://github.com/openresty/luajit2/archive/v2.1-20190530.tar.gz \
&& wget https://github.com/simplresty/ngx_devel_kit/archive/v0.3.1rc1.tar.gz \
&& wget https://github.com/openresty/lua-nginx-module/archive/v0.10.15.tar.gz \
&& wget https://github.com/openresty/stream-lua-nginx-module/archive/v0.0.7.tar.gz \ 
&& wget http://nginx.org/download/nginx-1.16.0.tar.gz \
&& ls *.tar.gz | xargs -n1 tar xzf \
&& cd luajit2-2.1-20190530/ && make && make install \
&& export LUAJIT_LIB=/usr/local/lib && export LUAJIT_INC=/usr/local/include/luajit-2.1 \
&& cd /usr/src/nginx-1.16.0/ \
&& ./configure --with-compat --with-ld-opt="-lpcre -Wl,-rpath,/usr/lib" --add-dynamic-module=../ngx_devel_kit-0.3.1rc1 --add-dynamic-module=../lua-nginx-module-0.10.15 \
&& make modules \
&& cp objs/*.so /etc/nginx/modules/ \
&& cd /usr/src/ \
&& wget https://github.com/openresty/lua-cjson/archive/master.zip -O lua-cjson.zip\
&& unzip lua-cjson.zip \
&& cd lua-cjson-master \
&& sed -i 's#(PREFIX)/include$#(PREFIX)/include/luajit-2.1#' Makefile \
&& make && make install \
&& mkdir -p /etc/nginx/lua/ \
&& cp cjson.so /etc/nginx/lua/ \
&& mkdir -p /usr/src/luapkgs/ && cd /usr/src/luapkgs/ \
&& wget https://github.com/openresty/lua-resty-redis/archive/master.zip -O lua-resty-redis.zip \
&& wget https://github.com/openresty/lua-resty-websocket/archive/master.zip -O lua-resty-websocket.zip \
&& wget https://github.com/openresty/lua-resty-mysql/archive/master.zip -O lua-resty-mysql.zip \
&& wget https://github.com/openresty/lua-resty-core/archive/master.zip -O lua-resty-core.zip \ 
&& wget https://github.com/openresty/lua-resty-lrucache/archive/master.zip -O lua-resty-lrucache.zip \ 
&& ls *.zip |xargs -n1 unzip -o \
&& cp -r */lib/* /etc/nginx/lua/ \
&& cd / && rm -rf /usr/src \
&& apk del .build-deps \
&& apk add --no-cache libgcc
