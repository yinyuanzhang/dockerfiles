FROM debian:latest

ENV NGINX_VERSION 1.15.5
ENV NGINX_PUSH_STREAM_MODULE_PATH /Sources/nginx-push-stream-module
ENV LUAJIT_VERSION 2.0
ENV LUAJIT_LIB /usr/local/lib
ENV LUAJIT_INC /usr/local/include/luajit-${LUAJIT_VERSION}

# Install packages
RUN apt-get update \
    && apt-get install -y \
       wget \
       git \
       gcc \
       build-essential \
       libc6 \
       libpcre3 \
       libpcre3-dev \
       libssl-dev \
       zlib1g \
       zlib1g-dev \
       lsb-base

# Install nginx-push-stream-module
RUN git clone https://github.com/wandenberg/nginx-push-stream-module.git \
    && git clone http://luajit.org/git/luajit-${LUAJIT_VERSION}.git  \
    && cd luajit-${LUAJIT_VERSION} \
    && make \
    && make install \
    && cd / && git clone https://github.com/openresty/lua-nginx-module.git \
    && mv /lua-nginx-module /usr/local/src/lua-nginx-module \
    && git clone https://github.com/simplresty/ngx_devel_kit.git \
    && mv /ngx_devel_kit /usr/local/src/ngx-devel-kit \
    && wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz \
    && tar xzvf nginx-${NGINX_VERSION}.tar.gz \
    && cd nginx-${NGINX_VERSION} \
    && ./configure --add-module=../nginx-push-stream-module --with-http_secure_link_module --with-http_ssl_module --with-ld-opt="-Wl,-rpath,$LUAJIT_LIB" --add-module=/usr/local/src/lua-nginx-module --add-module=/usr/local/src/ngx-devel-kit \
    && make \
    && make install

# Install certbot
RUN echo "deb http://deb.debian.org/debian stretch-backports main" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y certbot python-certbot-nginx -t stretch-backports \
  && apt-get install -y python3-certbot-dns-cloudflare

# Clean data
RUN apt-get purge -y \
    wget \
    git \
    gcc \
    && apt-get clean

EXPOSE 80

CMD ["/usr/local/nginx/sbin/nginx", "-c", "/usr/local/nginx/conf/nginx.conf"]

