FROM php:7.1-fpm

ENV COMPOSER_ALLOW_SUPERUSER=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils vim curl debconf subversion git apt-transport-https \
    build-essential locales acl mailutils wget zip unzip \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    less \
    gnupg gnupg1 gnupg2 \
    dnsutils

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  \
    && docker-php-ext-install -j$(nproc) gd mysqli pdo pdo_mysql

COPY php.ini /etc/php/7.1.23/php.ini
COPY php-fpm-pool.conf /etc/php/7.1.23/pool.d/www.conf

RUN curl -sSk https://getcomposer.org/installer | php -- --disable-tls && \
   mv composer.phar /usr/local/bin/composer

RUN groupadd dev -g 999
RUN useradd dev -g dev -d /home/dev -m

RUN rm -rf /var/lib/apt/lists/*
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen

WORKDIR /var/www/

EXPOSE 9000
CMD ["php-fpm"]
