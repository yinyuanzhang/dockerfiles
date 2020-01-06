FROM php:fpm

ARG INSTALL_XDEBUG=true
ENV INSTALL_XDEBUG ${INSTALL_XDEBUG}
RUN if [ ${INSTALL_XDEBUG} = true ]; then \
    pecl install xdebug && \
    docker-php-ext-enable xdebug \
;fi

RUN apt-get update && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng-dev \
	&& docker-php-ext-install -j$(nproc) iconv \
	&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
	&& docker-php-ext-install -j$(nproc) gd

RUN apt-get update && apt-get install -y libz-dev libmemcached-dev libjpeg-dev libpng-dev libxml2-dev libicu-dev libcurl4-gnutls-dev libzip-dev libzip4 \
    && pecl install memcached \
    && docker-php-ext-enable memcached \
    && docker-php-ext-install -j$(nproc) pdo pdo_mysql mysqli opcache \
    && docker-php-ext-enable pdo pdo_mysql mysqli opcache \
    && docker-php-ext-install -j$(nproc) mbstring bcmath json curl \
    && docker-php-ext-enable mbstring bcmath json curl \
    && docker-php-ext-configure intl \
    && docker-php-ext-install -j$(nproc) intl

RUN pecl install apcu \
    && docker-php-ext-enable apcu

RUN pecl install mcrypt-1.0.2 \
    && docker-php-ext-enable mcrypt

RUN docker-php-ext-install zip \
    && docker-php-ext-enable zip

RUN curl https://getcomposer.org/download/1.8.4/composer.phar > /tmp/composer.phar \
    && chmod +x /tmp/composer.phar \
    && mv /tmp/composer.phar /usr/local/bin/composer \
    && apt-get update && apt-get install -y less \
    && curl https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar > /tmp/wp-cli.phar \
    && chmod +x /tmp/wp-cli.phar \
    && mv /tmp/wp-cli.phar /usr/local/bin/wp

WORKDIR /var/www

CMD ["php-fpm"]

EXPOSE 9000
