FROM php:7.3-rc-cli
MAINTAINER Felix Dimmel

RUN pecl install xdebug-2.7.0beta1 \
    && echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20180731/xdebug.so' > \
        /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && php -m | grep xdebug