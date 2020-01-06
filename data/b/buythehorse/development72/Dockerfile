FROM ubuntu:xenial

RUN apt-get update -y \
    && apt-get install -y software-properties-common \
    && LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    unzip \
    git-core \
    curl \
    python-dev \
    graphicsmagick \
    build-essential \
    ca-certificates \
    php7.2 \
    php7.2-common \
    php7.2-cli \
    php7.2-curl \
    php7.2-gd \
    php7.2-mbstring \
    php7.2-json \
    php7.2-mysql \
    php7.2-sqlite \
    php7.2-xml \
    php7.2-zip \
    vim \
    unzip \
    curl \
    screen \
    openssl \
    apache2 \
    libapache2-mod-php7.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

## install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN mkdir -p /var/www/html
RUN chown -R www-data:www-data /var/www/html
VOLUME /var/www/html
WORKDIR /var/www/html

RUN usermod -u 1000 www-data
