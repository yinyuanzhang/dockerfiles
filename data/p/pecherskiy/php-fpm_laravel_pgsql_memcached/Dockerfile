FROM php:7.2-fpm
RUN apt-get update && apt-get install -y \
    git \
    libzip-dev \
    zip \
    unzip\
	libmsgpack-dev \
	libmsgpackc2 \
	zlib1g-dev \
	libmemcached-dev \
	libc-client-dev \
	libkrb5-dev \
	libmcrypt-dev \
	libpq-dev \
	libfreetype6-dev \
	libjpeg62-turbo-dev \
	libpng-dev \
	libicu-dev \
	libcurl4-nss-dev \
	libzmq3-dev \
	libyaml-dev \
    && docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install imap \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install -j$(nproc)  mbstring pdo_pgsql
	
RUN curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-memcached/archive/php7.tar.gz" && \
    mkdir -p /usr/src/php/ext/memcached && \
    tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1 && \
    docker-php-ext-configure memcached && \
    docker-php-ext-install memcached && \
    rm /tmp/memcached.tar.gz
	
RUN docker-php-ext-configure zip --with-libzip
RUN docker-php-ext-install pdo_mysql zip
RUN curl --silent --show-error https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer