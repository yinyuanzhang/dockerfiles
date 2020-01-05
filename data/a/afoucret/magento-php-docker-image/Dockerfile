ARG BASE_IMAGE=php:7.1-fpm
FROM $BASE_IMAGE

ENV PHP_MEMORY_LIMIT=2G \
    COMPOSER_ALLOW_SUPERUSER=1 \
    MAGENTO_ROOT=/var/www/magento \
    UPLOAD_MAX_FILESIZE=64M

RUN buildDeps=" \
      default-libmysqlclient-dev \
      libbz2-dev \
      libmemcached-dev \
      libsasl2-dev \
      libxslt-dev \
 " \
 && runtimeDeps=" \
       curl \
       cron \
       git \
       unzip \
       libfreetype6-dev \
       libicu-dev \
       libjpeg-dev \
       libldap2-dev \
       libmcrypt-dev \
       libmemcachedutil2 \
       libpng-dev \
       libpq-dev \
       libxml2-dev \
 " \
 && apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y $buildDeps $runtimeDeps \
 && docker-php-ext-install bcmath bz2 calendar iconv intl mbstring mcrypt mysqli opcache pdo_mysql pdo_pgsql pgsql soap zip xsl exif \
 && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
 && docker-php-ext-install gd \
 && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
 && docker-php-ext-install ldap \
 && pecl install memcached redis \
 && docker-php-ext-enable memcached.so redis.so \
 && pecl install -o -f xdebug \
 && apt-get purge -y --auto-remove $buildDeps \
 && rm -r /var/lib/apt/lists/*
