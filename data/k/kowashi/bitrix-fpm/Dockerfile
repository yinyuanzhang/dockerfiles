FROM selim13/bitrix-fpm
RUN rm /usr/local/etc/php/conf.d/memcache.ini && \
    apt-get update && \
    apt-get install libldap2-dev -y && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap && \
    docker-php-ext-install pdo_mysql && \
    docker-php-ext-install bcmath


RUN pecl install apcu \
    && pecl install apcu_bc-1.0.3 \
    && docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini \
    && docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini \
    && pecl install xdebug-2.7.1 \
    && docker-php-ext-enable xdebug --ini-name 10-docker-php-ext-xdebug.ini

RUN usermod -u 1000 www-data

# Clean repository
RUN apt-get clean \
&& rm -rf /var/lib/apt/lists/*