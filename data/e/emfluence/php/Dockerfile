FROM php:7.2-apache
LABEL maintainer="dev@emfluence.com"

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    libxml2-dev \
    mysql-client \
    && a2enmod rewrite \
    && mkdir -p /usr/local/etc/php/conf.d \
    && docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install \
    gd \
    mysqli \
    opcache \
    pdo \
    pdo_mysql \
    && pecl install redis \
    && docker-php-ext-enable redis \
    && rm -rf /usr/local/lib/conf.d \
    && ln -s /usr/local/etc/php/conf.d /usr/local/lib/conf.d \
    && apt-get -y clean \
    && apt-get -y autoclean \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* && rm -rf && rm -rf /var/lib/cache/* && rm -rf /var/lib/log/* && rm -rf /tmp/*

COPY apache2.conf /etc/apache2/apache2.conf

EXPOSE 80:80

CMD ["apache2-foreground"]
