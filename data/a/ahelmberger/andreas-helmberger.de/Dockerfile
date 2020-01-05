FROM node:8.11.2-alpine

MAINTAINER Andreas Helmberger <public@ahelmberger.de>

# Install nginx
ENV NGINX_VERSION nginx-1.9.5
RUN apk --update add openssl-dev pcre-dev zlib-dev wget build-base && \
    mkdir -p /tmp/src && \
    cd /tmp/src && \
    wget http://nginx.org/download/${NGINX_VERSION}.tar.gz && \
    tar -zxvf ${NGINX_VERSION}.tar.gz && \
    cd /tmp/src/${NGINX_VERSION} && \
    ./configure \
        --with-http_ssl_module \
        --with-http_gzip_static_module \
        --prefix=/etc/nginx \
        --http-log-path=/var/log/nginx/access.log \
        --error-log-path=/var/log/nginx/error.log \
        --sbin-path=/usr/local/sbin/nginx && \
    make && \
    make install && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    apk del wget build-base && \
    rm -rf /tmp/src && \
    rm -rf /var/cache/apk/*

WORKDIR /sources

COPY package.json /sources/package.json

RUN yarn install

COPY . /sources

RUN yarn run build && \
    mkdir /html && \
    mv -v ./build/* /html && \
    mv -v ./nginx.conf /etc/nginx/conf/nginx.conf && \
    rm -rf /sources

ENV VIRTUAL_HOST andreas-helmberger.de,www.andreas-helmberger.de

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
