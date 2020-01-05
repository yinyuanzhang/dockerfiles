FROM php:7.2-fpm-stretch

MAINTAINER Daniel Chodusov <daniel@chodusov.com>

# Install general packages
RUN apt-get update && apt-get install -y \
	libfreetype6-dev \
	libjpeg62-turbo-dev \
	libmcrypt-dev \
	libcurl4-gnutls-dev \
	pkg-config \
	libssl1.0-dev \
	gcc \
	make \
	autoconf \
	libc-dev \
    libxml2-dev \
    librabbitmq-dev \
    libssh-dev \
    unzip \
    mysql-client \
    zlib1g-dev \
    libicu-dev \
    g++ \
    wget \
    gnupg \
    software-properties-common \
    openssh-client \
    git-core

# Install APCU
ADD https://pecl.php.net/get/apcu-5.1.3.tgz /tmp/apcu.tar.gz
RUN mkdir -p /usr/src/php/ext/apcu\
  && tar xf /tmp/apcu.tar.gz -C /usr/src/php/ext/apcu --strip-components=1

RUN docker-php-ext-configure apcu\
  && docker-php-ext-install apcu

RUN rm -rd /usr/src/php/ext/apcu && rm /tmp/apcu.tar.gz

ADD https://pecl.php.net/get/apcu_bc-1.0.3.tgz /tmp/apcu_bc.tar.gz
RUN mkdir -p /usr/src/php/ext/apcu-bc\
  && tar xf /tmp/apcu_bc.tar.gz -C /usr/src/php/ext/apcu-bc --strip-components=1

RUN docker-php-ext-configure apcu-bc\
  && docker-php-ext-install apcu-bc

RUN rm -rd /usr/src/php/ext/apcu-bc && rm /tmp/apcu_bc.tar.gz

RUN rm /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini
RUN echo extension=apcu.so > /usr/local/etc/php/conf.d/20-php-ext-apcu.ini

# Install APC
RUN rm /usr/local/etc/php/conf.d/docker-php-ext-apc.ini
RUN echo extension=apc.so > /usr/local/etc/php/conf.d/21-php-ext-apc.ini

# Install other extensions
RUN docker-php-ext-install bcmath
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd
RUN docker-php-ext-install intl
RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install mysqli
RUN docker-php-ext-install curl
RUN docker-php-ext-install opcache
RUN docker-php-ext-install zip
RUN docker-php-ext-install xml
RUN docker-php-ext-install json
RUN docker-php-ext-install mbstring
RUN docker-php-ext-install sockets

# Install AMPQP support
RUN pecl install amqp \
&& docker-php-ext-enable amqp

# Install MongoDB extension
RUN pecl install mongodb \
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongodb.ini \
&& php -m | grep -i mongo

# Generate locales
RUN apt-get install locales -y
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "cs_CZ.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
