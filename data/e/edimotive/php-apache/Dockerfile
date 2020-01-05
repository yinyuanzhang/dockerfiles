FROM php:7.1-apache
LABEL maintainer Edimotive <developers@edimotive.com>

WORKDIR /var/www

# Configure Apache
RUN a2enmod rewrite\
    && a2dissite 000-default\
    && echo "ServerName localhost" >> /etc/apache2/apache2.conf\
    && mkdir /var/www/web

RUN apt-get update &&\
    apt-get install -y libicu-dev &&\
    docker-php-ext-install intl &&\
    docker-php-ext-install opcache &&\
    docker-php-ext-install mbstring &&\
    docker-php-ext-install pdo_mysql &&\
    docker-php-ext-install mysqli &&\
    docker-php-ext-install exif &&\
    docker-php-ext-install bcmath

### APCU ###################
RUN pecl channel-update pecl.php.net &&\
    pecl install apcu &&\
    docker-php-ext-enable apcu
RUN echo "extension=apcu.so" >> `php --ini | grep "Loaded Configuration" | sed -e "s|.*:\s*||"`
############################

#################### GB Library ###############
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd
###############################################



################# XDEBUG ######################
RUN yes | pecl install xdebug &&\
    echo "zend_extension="`find /usr/local/lib/php/extensions/ -iname 'xdebug.so'` > /usr/local/etc/php/conf.d/xdebug.ini

############ COMPOSER #########################
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php &&\
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer &&\
    rm -f composer-setup.php
###############################################

RUN  service apache2 restart
