FROM php:5.6-fpm

MAINTAINER billy@moonlightrambler.net

RUN apt-get update && apt-get install -y \
      bzip2 \
      libcurl4-openssl-dev \
      libfreetype6-dev \
      libicu-dev \
      libjpeg-dev \
      libmcrypt-dev \
      libpng12-dev \
      libpq-dev \
      libxml2-dev \
      mysql-client \
      unzip \
 && rm -rf /var/lib/apt/lists/*

#gpg key from hello@withknown.com
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "53DE 5B99 2244 9132 8B92  7516 052D B5AC 742E 3B47"

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
 && docker-php-ext-install exif gd intl mbstring mcrypt mysql opcache pdo_mysql zip json xmlrpc

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
  echo 'opcache.memory_consumption=128'; \
  echo 'opcache.interned_strings_buffer=8'; \
  echo 'opcache.max_accelerated_files=4000'; \
  echo 'opcache.revalidate_freq=60'; \
  echo 'opcache.fast_shutdown=1'; \
  echo 'opcache.enable_cli=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini

# PECL extensions
RUN pecl install APCu-4.0.10 \
 && docker-php-ext-enable apcu

ENV KNOWN_VERSION 0.9.9
VOLUME /var/www/html

RUN curl -o known.zip -fSL http://assets.withknown.com/releases/known-${KNOWN_VERSION}.zip \
 && curl -o known.zip.sig -fSL http://assets.withknown.com/releases/known-${KNOWN_VERSION}.zip.sig \
 && gpg --batch --verify known.zip.sig known.zip \
 && unzip known.zip -d /usr/src/known/ \
 && rm known.zip*

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["php-fpm"]
