FROM php:5.6-fpm

RUN pecl install -o -f redis \
&&  rm -rf /tmp/pear \
&&  docker-php-ext-enable redis

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \
    && apt-get install -y --no-install-recommends apt-utils \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libcurl4-nss-dev \
        libicu-dev \
        libxslt-dev \
    && apt-get install -y \
    libxml2-dev \
    && docker-php-ext-install soap \
    && docker-php-ext-install iconv mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install curl \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install pdo pdo_mysql \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install soap \
    && docker-php-ext-install json \
    && docker-php-ext-install xsl \
    && docker-php-ext-install zip \
    && docker-php-ext-install opcache \
    && apt-get install -y zlib1g-dev libicu-dev g++ \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl \
    && cd /tmp \
CMD ["/usr/local/sbin/php-fpm", "--nodaemonize"]

RUN pecl install xdebug-2.5.5
RUN docker-php-ext-enable xdebug

RUN curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

RUN apt-get install -y vim
