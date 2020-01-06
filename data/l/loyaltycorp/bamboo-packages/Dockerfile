FROM php:7.3

# Update apt sources
RUN apt-get update -y

# Install os packages
RUN apt-get install -y bc git libicu-dev libmemcached-dev libzip-dev zlib1g-dev

# Install php extensions
RUN docker-php-ext-install bcmath \
    && docker-php-ext-install intl \
    && docker-php-ext-install zip \
    && echo "" | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo '' | pecl install memcached \
    && echo "extension=$(find /usr/local/lib/php/extensions/ -name memcached.so)" > /usr/local/etc/php/conf.d/memcached.ini

# Increase memory limit
RUN echo "memory_limit=2G" > /usr/local/etc/php/php.ini

# Install composer
RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/local/bin/ --filename=composer
