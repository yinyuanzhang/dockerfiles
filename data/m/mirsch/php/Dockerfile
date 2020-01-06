FROM php:7.3-fpm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    locales curl wget git zip unzip less \
    sudo

RUN docker-php-ext-configure pdo_mysql \
    && docker-php-ext-install -j$(nproc) pdo_mysql

RUN apt-get install -y --no-install-recommends \
    libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN docker-php-ext-configure bcmath \
    && docker-php-ext-install -j$(nproc) bcmath

RUN apt-get install -y --no-install-recommends \
    libc-client-dev libkrb5-dev \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install -j$(nproc) imap

RUN apt-get install -y --no-install-recommends \
    libldap2-dev \
    && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
    && docker-php-ext-install -j$(nproc) ldap

RUN apt-get install -y --no-install-recommends \
    zlib1g-dev libicu-dev g++ \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl

RUN apt-get install -y --no-install-recommends \
    zlib1g-dev libzip-dev \
    && docker-php-ext-configure zip \
    && docker-php-ext-install zip

RUN rm -rf /var/lib/apt/lists/*

COPY php.ini /usr/local/etc/php/php.ini

RUN curl -sSk https://getcomposer.org/installer | php -- --disable-tls && \
	mv composer.phar /usr/local/bin/composer

RUN wget -q --no-check-certificate https://phar.phpunit.de/phpunit-8.phar && \
    mv phpunit*.phar phpunit.phar && \
    chmod +x phpunit.phar && \
    mv phpunit.phar /usr/local/bin/phpunit

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen

RUN groupadd dev -g 999 && useradd dev -g dev -d /home/dev -m && passwd -d dev && echo "dev ALL=(ALL) ALL" > /etc/sudoers

WORKDIR /var/www/

EXPOSE 9000
CMD ["php-fpm"]
USER dev
