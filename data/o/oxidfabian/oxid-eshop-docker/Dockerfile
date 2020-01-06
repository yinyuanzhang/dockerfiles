FROM oxidfabian/oxid-php:7.1 as builder

RUN composer create-project --no-interaction --no-dev oxid-esales/oxideshop-project /var/www/html/ dev-b-6.1-ce

FROM php:7.1-apache

ENV APACHE_DOCUMENT_ROOT /var/www/html/source
ENV PROTOCOL https
ENV MYSQL_HOST db
ENV OXID_DOMAIN myoxidshop.de
ENV OXID_DEMODATA false
ENV OXID_ADMIN_PASSWORD admin
ENV USE_REDIS false
ENV REDIS_HOST redis-host

# install dependencies and cleanup (needs to be one step, as else it will cache in the laver)
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    git ssmtp mysql-client iproute2 libfreetype6 libjpeg62-turbo libcurl4-openssl-dev libjpeg-dev libpng-dev libxml2-dev libmemcached-dev && \
    pecl install xdebug memcached && \
    docker-php-ext-enable xdebug && \
    docker-php-ext-configure gd --with-jpeg-dir=/usr/local/ && \
    docker-php-ext-install -j$(nproc) curl json xml mbstring zip bcmath soap pdo_mysql gd && \
    apt-get clean && \
    apt-get autoremove -y && \
    apt-get purge -y --auto-remove libcurl4-openssl-dev libjpeg-dev libpng-dev libxml2-dev libmemcached-dev && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder --chown=www-data:www-data /var/www/html /var/www/html

COPY docker-php-entrypoint /usr/local/bin/
COPY config.inc.php /var/www/config.inc.php

RUN chmod 777 /usr/local/bin/docker-php-entrypoint \
    && ln -s /usr/local/bin/docker-php-entrypoint /