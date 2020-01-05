FROM php:7.0-fpm
MAINTAINER Simone Bembi <simone.bembi@gmail.com>

RUN docker-php-ext-install mysqli pdo pdo_mysql pcntl \
	&& pecl install xdebug \
	&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini

COPY php-fpm.conf /usr/local/etc/php-fpm.conf
COPY www.conf /usr/local/etc/php-fpm.d/www.conf

CMD ["php"]