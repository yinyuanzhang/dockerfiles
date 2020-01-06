FROM alpine:edge
MAINTAINER Onni Hakala <onni.hakala@keksi.io>

RUN \
	##
    # Install php7
    # - These repositories are in 'testing' repositories but it's much more stable/easier than compiling our own php.
    ##
    apk add --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ \
    php7 php7-fpm \
    php7-session php7-opcache php7-phar \
    php7-mcrypt php7-curl php7-zlib php7-openssl \
    php7-soap php7-json php7-xml php7-xmlreader php7-simplexml \
    php7-pdo_mysql php7-mysqli php7-mysqlnd php7-pdo \
    php7-redis php7-mongodb php7-memcached \
    php7-mbstring php7-intl php7-iconv \
    php7-gd php7-dom \
    php7-ctype php7-zip \

    # Used by phpunit tests
    php7-tokenizer \

    && apk add --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ \
    php7-xdebug \
   	
    # Install mail client and dev dependencies
    && apk add --update curl msmtp bash \

    ##
    # Install composer
    ##
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer global require hirak/prestissimo \

    # Remove cache and tmp files
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

ENV PORT=9000 \
	PROJECT_ROOT=/var/www/project \
	XDEBUG_REMOTE_PORT=9000 \
	PHP_DISPLAY_ERRORS=1

RUN set -ex \
	# Allow more resources for php-fpm
    && cd /etc/php7 \
	&& sed -i '/^pm.max_children/c\pm.max_children = 5' php-fpm.d/www.conf \
	&& sed -i '/^pm.min_spare_servers/c\pm.min_spare_servers = 1' php-fpm.d/www.conf \
	&& sed -i '/^pm.max_spare_servers/c\pm.max_spare_servers = 2' php-fpm.d/www.conf

COPY rootfs/ /

COPY entrypoint.sh /

EXPOSE ${PORT}
WORKDIR ${PROJECT_ROOT}

ENTRYPOINT /entrypoint.sh
CMD ["php-fpm7"]