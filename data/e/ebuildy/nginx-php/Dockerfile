FROM debian:8

RUN apt-get update && \
	apt-get install -y \
		curl

# Setup repos
RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add - && \
	echo "deb http://nginx.org/packages/debian/ jessie nginx" > /etc/apt/sources.list.d/nginx.list && \
	echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list.d/nginx.list && \
	echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list && \
    curl -sL https://www.dotdeb.org/dotdeb.gpg | apt-key add -

# Add s6 overlay
RUN mkdir -p /opt/s6 && \
	curl -sL "https://github.com/just-containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz" | \
		tar xz --strip-component 1 -C /

# Remove php5 stuff
RUN DEBIAN_FRONTEND=noninteractive \
	apt-get autoremove --purge php5*

# Install softwares
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends \
    	nginx=1.10.* \
		php7.0-curl* \
        php7.0-fpm \
        php7.0-gd \
        php7.0-geoip \
        php7.0-json \
        php7.0-mysql \
        php7.0-mcrypt \
        php7.0-memcached \
        php7.0-intl \
        php7.0-xml

ADD nginx 		/etc/services.d/nginx
ADD php 		/etc/services.d/php

ENTRYPOINT ["/init"]

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/www && \
    echo "<?php phpinfo(); " > /var/www/index.php && \
    chown -R www-data:www-data /var/www

EXPOSE 80

HEALTHCHECK CMD curl --fail http://localhost/ || exit 1