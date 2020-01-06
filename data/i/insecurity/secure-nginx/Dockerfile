FROM insecurity/debian:stretch
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>

# Set variables (Choose version in: http://nginx.org/packages/debian/pool/nginx/n/nginx/)
ARG BUILD=1.16.0
ARG VERSION=$BUILD-1
ARG NGINX_VERSION=$VERSION~stretch

# Install temporarly dev libraries (stretch)
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
      ca-certificates gnupg lsb-release libc6-dev dpkg-dev build-essential:native debhelper dh-systemd quilt libpcre3-dev zlib1g-dev \

# Add temporarily Sid/Unstable repository just for OpenSSL 1.1.1 and TLS 1.3 support \
  && echo "deb http://deb.debian.org/debian unstable main" >> /etc/apt/sources.list \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y openssl libssl1.1 libssl-dev \

# Get, patch, recompile and install Nginx source package to support TLS 1.3 \
  && curl -O https://nginx.org/keys/nginx_signing.key && apt-key add ./nginx_signing.key && rm ./nginx_signing.key \
  && echo "deb http://nginx.org/packages/debian/ $(lsb_release -sc) nginx" >> /etc/apt/sources.list \
  && echo "deb-src http://nginx.org/packages/debian/ $(lsb_release -sc) nginx" >> /etc/apt/sources.list \
  && apt-get update \
    && mkdir /tmp/nginx && cd /tmp/nginx && apt-get source nginx=${NGINX_VERSION} \
    && cd nginx-${BUILD} \
    && sed -e 's#--with-ld-opt="$(LDFLAGS)"#--with-ld-opt="$(LDFLAGS)" --with-openssl-opt\=enable-tls1_3#g' debian/rules \
    && dpkg-buildpackage -b \
    && dpkg -i ../nginx_${NGINX_VERSION}_amd64.deb \
    && cd / && rm -r /tmp/nginx \

# Remove unstable, deb-src repositories and install nginx modules \
  && sed -i -e'/unstable\|deb-src/d' /etc/apt/sources.list \
  && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests -y \
    gettext-base \
    nginx-module-xslt=${NGINX_VERSION} \
    nginx-module-geoip=${NGINX_VERSION} \
    nginx-module-image-filter=${NGINX_VERSION} \
    nginx-module-perl=${NGINX_VERSION} \
#    nginx-module-njs=${NGINX_VERSION} \

# Clean unnecessary dev packages \
  && apt-get remove -y --purge lsb-release gnupg dpkg-dev build-essential:native debhelper dh-systemd quilt libssl-dev libpcre3-dev zlib1g-dev libc6-dev \

# Security - Fix UID/GID of nginx user \
  && usermod -u 3005 nginx \
    && groupmod -g 3005 nginx \
    && chown -R nginx:nginx /etc/nginx/ \
    && chown -R nginx:nginx /var/cache/nginx/ \
    && chown -R nginx:nginx /var/log/nginx/ \
    && chmod -R 777 /var/log/nginx/ \

# Security - Edit default configuration file for non-root usage
  && sed -i -e "s#\(listen.*80\)#listen       8080#" /etc/nginx/conf.d/default.conf \
    && sed -i -e "s#\(/var/run\)#/etc/nginx#" /etc/nginx/nginx.conf \

# Persistence - Save a copy of default configuration/www files \
  && mkdir -p /usr/local/bak/etc/ && mkdir -p /usr/local/bak/usr/ \
  && cp -r /etc/nginx/ /usr/local/bak/etc/ \
    && cp -r /usr/share/nginx/ /usr/local/bak/usr/nginx/ \
    && chown -R nginx:nginx /usr/local/bak/ \

# Persistence - Add run script \
  && echo '#!/bin/bash' > /run.sh \
    && echo 'echo "Create configuration and content dir if missing in volumes..."' >> /run.sh \
    && echo 'cp -rn /usr/local/bak/etc/nginx/ /etc/' >> /run.sh \
    && echo 'cp -rn /usr/local/bak/usr/nginx/ /usr/share/' >> /run.sh \
    && echo 'echo "Reset permissions..."' >> /run.sh \
    && echo 'chown -R nginx:nginx /var/cache/nginx/' >> /run.sh \
    && echo 'exec /usr/sbin/nginx & tail -F /var/log/nginx/*' >> /run.sh \
    && chmod 755 /run.sh \

# Forward request and error logs to docker log collector \
#  && ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log \

# APT Clean-up \
  && apt-get autoclean \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set listening ports inside container
EXPOSE 8080 8443

# Let's go !
CMD ["/run.sh"]
