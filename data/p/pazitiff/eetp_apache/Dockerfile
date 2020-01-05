FROM php:7.1.26-apache

# SSL
COPY ./ssl/server.pem /etc/ssl/certs/server.pem
COPY ./ssl/server.key /etc/ssl/private/server.key
COPY ./ssl/server.crt /usr/local/share/ca-certificates/server.crt
COPY ./ssl/server.crt /usr/share/ca-certificates/server.crt
RUN chmod 0600 /etc/ssl/private/server.key
RUN update-ca-certificates

# PHP extensions
RUN apt-get update && apt-get install -y \
        telnet \
        git \
        curl \
        wget \
        vim \
        iputils-ping \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
#        mysql-client \
#        postgresql-client \
#        php-soap \
        libxml2-dev \
        libpq-dev \
        libmemcached-dev \
        zlib1g-dev \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /download/directory \
    && docker-php-ext-install -j$(nproc) mbstring tokenizer mcrypt iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install exif \
    && docker-php-ext-install zip \
    && docker-php-ext-install opcache \
    && docker-php-ext-install pdo \
    && docker-php-ext-install pdo_pgsql \
#    && docker-php-ext-install pdo_mysql mysqli \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && pecl install memcached-3.0.3 \
    && docker-php-ext-enable memcached \
    && mkdir /usr/share/man/man1 \
    && mkdir /usr/share/man/man7 \
#    && pecl install -o -f redis \
#    && docker-php-ext-enable redis
    && rm -f /etc/apache2/sites-available/000-default.conf \
    && rm -f /etc/apache2/sites-available/default-ssl.conf \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');" \
    && usermod -u 1000 www-data \
    && groupmod -g 1000 www-data \
    && a2enmod rewrite \
    && a2enmod ssl


COPY ./config/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY ./config/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
COPY ./config/php.ini /usr/local/etc/php/php.ini

RUN a2ensite default-ssl

# Московское время
RUN ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
#ENV DRUSH_VERSION 8.1.2
#RUN curl -L --silent https://github.com/drush-ops/drush/releases/download/${DRUSH_VERSION}/drush.phar \
#  > /usr/local/bin/drush && chmod +x /usr/local/bin/drush