FROM debian:wheezy

# apt stuff...
RUN export DEBIAN_FRONTEND=noninteractive \
    && echo 'force-unsafe-io' > /etc/dpkg/dpkg.cfg.d/02apt-speedup \
    && echo "deb http://http.debian.net/debian/ wheezy-backports main" > /etc/apt/sources.list.d/backports.list \
    && echo "deb-src http://http.debian.net/debian/ wheezy main" > /etc/apt/sources.list.d/src.list \
    && echo "deb-src http://http.debian.net/debian/ wheezy-backports main" >> /etc/apt/sources.list.d/src.list \
    && apt-get update \
    && apt-get -y install --no-install-recommends build-essential curl ca-certificates \
    && apt-get -y -t wheezy-backports build-dep nginx \
    && apt-get -q -y clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* \
    && rm -rf /usr/share/man/?? /usr/share/man/??_*

# download & compile ngix...
COPY ngx_modules /root/ngx_modules
COPY ngx_source /root/ngx_source
RUN cd /root/ngx_source \
    && ./auto/configure \
      --with-cc-opt="$(dpkg-buildflags --get CFLAGS) $(dpkg-buildflags --get CPPFLAGS)" \
      --with-ld-opt="$(dpkg-buildflags --get LDFLAGS)" \
      --prefix=/usr/local \
      --sbin-path=/usr/local/sbin \
      --conf-path=/etc/nginx/nginx.conf \
      --http-log-path=/var/log/nginx/access.log \
      --error-log-path=/var/log/nginx/error.log \
      --lock-path=/var/lock/nginx.lock \
      --pid-path=/run/nginx.pid \
      --http-client-body-temp-path=/var/lib/nginx/body \
      --http-fastcgi-temp-path=/var/lib/nginx/fastcgi \
      --http-proxy-temp-path=/var/lib/nginx/proxy \
      --http-scgi-temp-path=/var/lib/nginx/scgi \
      --http-uwsgi-temp-path=/var/lib/nginx/uwsgi \
      --with-debug \
      --with-pcre-jit \
      --with-ipv6 \
      --with-http_ssl_module \
      --with-http_stub_status_module \
      --with-http_realip_module \
      --with-http_auth_request_module \
      --with-http_addition_module \
      --with-http_geoip_module \
      --with-http_gzip_static_module \
      --with-http_image_filter_module \
      --with-http_sub_module \
      --with-http_xslt_module \
      --add-module=/root/ngx_modules/ngx_devel_kit \
      --add-module=/root/ngx_modules/lua-nginx-module \
      --add-module=/root/ngx_modules/ngx_aws_auth \
    && make -j2 \
    && make install \
    && rm -rf /root/ngx_modules /root/ngx_source \
    && mkdir --parents /var/lib/nginx

# use envplate to configure buckets from env vars (https://github.com/kreuzwerker/envplate)
COPY config/ep-v0.0.4-linux /usr/local/bin/ep
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY config/mime.types /etc/nginx/mime.types

RUN useradd www

EXPOSE 80 443
CMD [ "ep", "-v", "/etc/nginx/nginx.conf", "--", "/usr/bin/env", "nginx", "-g", "daemon off;" ]
