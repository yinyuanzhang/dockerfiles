FROM php:7.2-fpm
MAINTAINER Kamil <kamil@kingfisherdirect.co.uk>

# add magento settings
COPY config/magento.ini $PHP_INI_DIR/conf.d/

# composer:          unzip git
# gd dependencies:   libfreetype6-dev libjpeg62-turbo-dev libpng-dev
# intl dependendies: libicu-dev
# simplexml:         libxml2
# xsl:               libxslt-dev
# sodium:            libsodium-dev
# zip:               libzip-dev

RUN apt-get update && \
  apt-get install -y \
    cron \
    unzip \
    git \
    libfreetype6-dev libjpeg62-turbo-dev libpng-dev \
    libicu-dev \
    libxml2 \
    libxslt-dev \
    libsodium-dev \
    libzip-dev

RUN pecl install -f libsodium

RUN docker-php-ext-configure zip --with-libzip && \
  docker-php-ext-configure \
    gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

RUN docker-php-ext-install \
  bcmath \
  gd \
  intl \
  opcache \
  pdo_mysql \
  soap \
  xsl \
  zip

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY bin/cronstart /usr/local/bin/
COPY bin/magento-entrypoint /usr/local/bin/
COPY bin/magento-setup /usr/local/bin/

RUN chmod +x /usr/local/bin/cronstart
RUN chmod +x /usr/local/bin/magento-entrypoint
RUN chmod +x /usr/local/bin/magento-setup

RUN groupadd -g 1000 app \
    && useradd -g 1000 -u 1000 -d /var/www -s /bin/bash app

# Production

# default to php production settings
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

VOLUME /var/www/html/pub/media

ENTRYPOINT ["magento-entrypoint"]

# End Production

USER app:app
