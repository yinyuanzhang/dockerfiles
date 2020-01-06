FROM nginx:1.16-alpine AS builder

ENV NAXSI_VERSION 0.56
ENV VTS_VERSION 0.1.18

# Download sources
RUN wget "http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz" -O nginx.tar.gz && \
    wget "https://github.com/nbs-system/naxsi/archive/${NAXSI_VERSION}.tar.gz" -O naxsi.tar.gz && \
    wget "https://github.com/vozlt/nginx-module-vts/archive/v${VTS_VERSION}.tar.gz" -O vts.tar.gz

RUN  apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                make \
                openssl-dev \
                pcre-dev \
                zlib-dev \
                linux-headers \
                libxslt-dev \
                gd-dev \
                geoip-dev \
                perl-dev \
                libedit-dev \
                mercurial \
                bash \
                alpine-sdk \
                findutils

RUN mkdir /usr/src && tar -zxC /usr/src -f nginx.tar.gz && \
    tar -zxC /usr/src -f naxsi.tar.gz && \
    tar -zxC /usr/src -f vts.tar.gz && \
    cp /usr/src/naxsi-${NAXSI_VERSION}/naxsi_config/naxsi_core.rules /etc/nginx && \
    cd /usr/src/nginx-${NGINX_VERSION} && \
    ./configure --with-compat --add-dynamic-module=/usr/src/naxsi-${NAXSI_VERSION}/naxsi_src/ --add-dynamic-module=/usr/src/nginx-module-vts-${VTS_VERSION} && \
    make && make install

FROM nginx:1.16-alpine

COPY --from=builder /usr/local/nginx/modules/ngx_http_vhost_traffic_status_module.so /usr/local/nginx/modules/ngx_http_vhost_traffic_status_module.so

COPY --from=builder /usr/local/nginx/modules/ngx_http_naxsi_module.so /usr/local/nginx/modules/ngx_http_naxsi_module.so

COPY --from=builder /etc/nginx/naxsi_core.rules /etc/nginx

COPY nginx.conf /etc/nginx/nginx.conf

COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
