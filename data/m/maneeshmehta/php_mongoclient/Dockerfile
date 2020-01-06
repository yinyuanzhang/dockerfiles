FROM php:7.1-fpm

RUN apt-get update && apt-get install --yes --no-install-recommends \
libssl-dev \
libpng-dev \
libjpeg-dev \
libpq-dev \
libmcrypt-dev \
libldap2-dev \
libldb-dev \
libicu-dev \
libgmp-dev \
libxslt-dev \
libmagickwand-dev \
libmagickwand-dev \
libmemcached-dev zlib1g-dev \
&& docker-php-ext-install mbstring opcache \
&& pecl install mongodb redis \
&& docker-php-ext-enable redis mongodb.so \
&& docker-php-ext-install mysqli \
&& docker-php-ext-install gd \
opcache \
pdo \
pdo_mysql \
pdo_pgsql \
pcntl \
intl \
mcrypt \
exif \
soap \
xsl \
zip \
&& pecl install imagick \
&& docker-php-ext-enable imagick \
&& pecl install memcached-3.0.3 \
&& docker-php-ext-enable memcached \
