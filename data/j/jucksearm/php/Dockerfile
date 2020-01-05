FROM php:7.1.2-apache

MAINTAINER jucksearm.bkk@gmail.com

ENV APACHE_DOC_ROOT /var/www/html

RUN apt-get update \
    && apt-get -y install \
	apt-utils \
	git \
        g++ \
        libxml2-dev \
        libicu-dev \
        libmcrypt-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng12-dev \
        libc-client-dev \
        libkrb5-dev \
        zlib1g-dev \
        npm \
    --no-install-recommends \

    # install bower
    && ln -s /usr/bin/nodejs /usr/bin/node \
    && npm install -g bower \

    # Enable mod_rewrite
    && a2enmod rewrite \

    # Install PHP extensions
    && docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos \
    && docker-php-ext-install imap soap iconv mcrypt intl pdo_mysql mbstring opcache zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && pecl install apcu-5.1.3 && echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini \

    && apt-get purge --auto-remove -y gcc make \
    && rm -r /var/lib/apt/lists/* \
    && apt-get clean \

    # Fix write permissions with shared folders
    && usermod -u 1000 www-data

# Next composer and global composer package, as their versions may change from time to time
RUN curl -sS https://getcomposer.org/installer | php \
    && chmod +x composer.phar \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require "fxp/composer-asset-plugin:^1.2.0"

COPY ./php.ini /usr/local/etc/php/

COPY ./start /usr/local/bin/

RUN chmod u+x /usr/local/bin/start

COPY ./git-setup /usr/local/bin/

RUN chmod u+x /usr/local/bin/git-setup

CMD ["start"]
