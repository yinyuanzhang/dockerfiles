FROM php:7.2.14-apache
RUN fetchDeps=" \
        libicu-dev \
        libbz2-dev \
        libssh2-1-dev \
        libssl-dev \
	" \
    && apt-get update && apt-get install -y $fetchDeps \
        librabbitmq-dev \
        libxml2-dev \
        libpq-dev \
        libssh2-1 \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        unzip \
        git \
        --no-install-recommends && rm -r /var/lib/apt/lists/* \
    && a2enmod rewrite \
    && docker-php-ext-install bcmath bz2 calendar exif opcache pdo_mysql pdo_pgsql intl zip soap \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && pecl install redis \
    && pecl install mongodb \
    && pecl install amqp \
    && pecl install ssh2-1.1.2 \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $fetchDeps \
    && docker-php-ext-enable redis mongodb amqp ssh2
RUN pecl install https://xdebug.org/files/xdebug-2.6.1.tgz \
    && docker-php-ext-enable xdebug \
    && echo "error_reporting = E_ALL" > /usr/local/etc/php/php.ini \
    && echo "display_startup_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "display_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "expose_php = Off" >> /usr/local/etc/php/php.ini \
    && echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN sed -i 's/\/var\/www\/html/\/var\/www\/public/g' /etc/apache2/sites-available/000-default.conf \
    && mv /var/www/html /var/www/public
