FROM php:7-apache

MAINTAINER Adam Zammit <adam.zammit@acspri.org.au>

#Install requirements above base
RUN apt-get update && apt-get install -y libzip-dev libpng-dev libjpeg-dev bzr wget unzip libxslt-dev && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install xsl opcache zip gd

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=2'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
        echo 'display_errors=Off'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini


RUN mkdir /images && chown www-data:www-data /images

RUN wget https://github.com/tecnickcom/TCPDF/archive/master.zip && \
    unzip master.zip && \
    mv TCPDF-master /var/lib/tcpdf && \
    rm master.zip

RUN set -x \
  && bzr branch lp:quexml /usr/src/quexml \
  && chown -R www-data:www-data /usr/src/quexml

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat

# ENTRYPOINT resets CMD
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]
