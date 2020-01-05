FROM php:7.4-fpm
LABEL Jabsouliman <benjamin.souliman@gmail.com>

RUN apt-get update
RUN apt-get install -y \
        unzip \
        vim

RUN docker-php-ext-enable opcache
RUN docker-php-ext-install calendar
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install tokenizer
RUN docker-php-ext-install json

RUN apt-get install -y \
        libonig-dev \
    && docker-php-ext-install iconv mbstring

RUN apt-get install -y \
        libcurl4-openssl-dev \
    && docker-php-ext-install curl

RUN apt-get install -y \
        libssl-dev \
    && docker-php-ext-install ftp phar

RUN apt-get install -y \
        libicu-dev \
    && docker-php-ext-install intl

RUN apt-get install -y \
        libmcrypt-dev \
    && docker-php-ext-install session

RUN apt-get install -y \
        libxml2-dev \
    && docker-php-ext-install simplexml xml xmlrpc

RUN apt-get install -y \
        libzip-dev \
        zlib1g-dev \
    && docker-php-ext-install zip

RUN apt-get install -y \
        libgmp-dev \
    && docker-php-ext-install gmp

RUN apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) gd

RUN apt-get install -y libmagickwand-dev
RUN pecl install imagick && docker-php-ext-enable imagick

ENV COMPOSER_BINARY=/usr/local/bin/composer \
    COMPOSER_HOME=/usr/local/composer
ENV PATH $PATH:$COMPOSER_HOME

RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar $COMPOSER_BINARY && \
    chmod +x $COMPOSER_BINARY

COPY php.fpm.ini /etc/php7/fpm/php.ini
COPY php.cli.ini /etc/php7/cli/php.ini

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/www

EXPOSE 9000

CMD ["php-fpm", "-F", "-c", "/etc/php7/fpm"]