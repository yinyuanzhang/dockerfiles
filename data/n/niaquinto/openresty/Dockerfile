FROM niaquinto/luarocks:2.2
MAINTAINER Tor Hveem <tor@hveem.no>
ENV REFRESHED_AT 2013-12-12

# Openresty (Nginx)
ENV OPENRESTY_HASH bca1744196acfb9e986f1fdbee92641e
ENV OPENRESTY_VERSION 1.7.10.2
RUN echo "deb-src http://httpredir.debian.org/debian jessie main" >> /etc/apt/sources.list && \
    echo "deb-src http://httpredir.debian.org/debian jessie-updates main" >> /etc/apt/sources.list && \
    echo "deb-src http://security.debian.org jessie/updates main" >> /etc/apt/sources.list && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libpq-dev && \
    apt-get build-dep -y nginx && \
    wget http://openresty.org/download/ngx_openresty-${OPENRESTY_VERSION}.tar.gz && \
    echo "${OPENRESTY_HASH} ngx_openresty-${OPENRESTY_VERSION}.tar.gz" > ngx_openresty-${OPENRESTY_VERSION}.md5 && \
    md5sum -c ngx_openresty-${OPENRESTY_VERSION}.md5 && \
    tar xvfz ngx_openresty-${OPENRESTY_VERSION}.tar.gz && \
    cd ngx_openresty-${OPENRESTY_VERSION} && \ 
    ./configure --with-luajit  --with-http_addition_module --with-http_dav_module --with-http_geoip_module --with-http_gzip_static_module --with-http_image_filter_module --with-http_realip_module --with-http_stub_status_module --with-http_ssl_module --with-http_sub_module --with-http_xslt_module --with-ipv6 --with-http_postgres_module --with-pcre-jit && \
    make && make install

EXPOSE 80
EXPOSE 443
CMD /usr/local/openresty/nginx/sbin/nginx -p `pwd` -c nginx.conf
