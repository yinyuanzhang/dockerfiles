FROM php:7.1-apache

RUN apt-get update && apt-get install -y \
        git \
        libmcrypt-dev \
        zip \
        zlib1g-dev && \
    docker-php-ext-install -j$(nproc) \
        mbstring \
        mysqli \
        pdo_mysql \
        zip && \
    pecl install xdebug-2.5.5 && docker-php-ext-enable xdebug && \
    pecl install mcrypt-1.0.0 && docker-php-ext-enable mcrypt && \
    echo "memory_limit=-1" >> /usr/local/etc/php/conf.d/memory-limit-php.ini

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    curl -sLo phpunit https://phar.phpunit.de/phpunit-5.phar && chmod +x phpunit && mv phpunit /usr/local/bin/phpunit
