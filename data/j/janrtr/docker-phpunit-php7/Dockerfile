FROM php:7.1-cli
MAINTAINER Chris Allan <chris@allan.codes>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y git libssh2-1 libssh2-1-dev && \
    pecl install ssh2-1.1.2 && \
    docker-php-ext-enable ssh2

RUN apt-get update -yqq \
    && apt-get install git zlib1g-dev libsqlite3-dev libpq-dev -y \
    && docker-php-ext-install zip \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install pdo_sqlite \
    && docker-php-ext-install pdo pdo_pgsql pgsql

RUN curl -fsSL https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require phpunit/phpunit ^6 --no-progress --no-scripts --no-interaction

RUN pecl install xdebug \
    && echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20160303/xdebug.so' > \
        /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && php -m | grep xdebug

ENV PATH /root/.composer/vendor/bin:$PATH
CMD ["phpunit"]
