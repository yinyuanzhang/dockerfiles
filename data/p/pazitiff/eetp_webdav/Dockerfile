FROM nginx

MAINTAINER Vladimir Chemeris <chamav@gmail.com>

ENV NGINX_DAV_EXT_MODULE_VERSION=0.1.0

# Install basic packages and build tools
RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
      telnet \
      wget \
      build-essential \
      libssl-dev \
      libpcre3 \
      ca-certificates \
      zlib1g-dev \
      libpcre3-dev \
      libexpat1-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# download and extract sources
RUN NGINX_VERSION=`nginx -V 2>&1 | grep "nginx version" | awk -F/ '{ print $2}'` && \
    cd /tmp && \
    wget http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz && \
    wget https://github.com/arut/nginx-dav-ext-module/archive/v$NGINX_DAV_EXT_MODULE_VERSION.tar.gz \
         -O nginx-dav-ext-module-$NGINX_DAV_EXT_MODULE_VERSION.tar.gz && \
    tar -xf nginx-$NGINX_VERSION.tar.gz && \
    mv nginx-$NGINX_VERSION nginx && \
    rm nginx-$NGINX_VERSION.tar.gz && \
    tar -xf nginx-dav-ext-module-$NGINX_DAV_EXT_MODULE_VERSION.tar.gz && \
    mv nginx-dav-ext-module-$NGINX_DAV_EXT_MODULE_VERSION nginx-dav-ext-module && \
    rm nginx-dav-ext-module-$NGINX_DAV_EXT_MODULE_VERSION.tar.gz

# configure and build
RUN cd /tmp/nginx && \
    BASE_CONFIGURE_ARGS=`nginx -V 2>&1 | grep "configure arguments" | cut -d " " -f 3-` && \
    /bin/sh -c "./configure ${BASE_CONFIGURE_ARGS} --add-module=/tmp/nginx-dav-ext-module" && \
    make && make install && \
    rm -rf /tmp/nginx*

COPY nginx.conf /etc/nginx/nginx.conf
COPY sites/*.conf /etc/nginx/sites-available/