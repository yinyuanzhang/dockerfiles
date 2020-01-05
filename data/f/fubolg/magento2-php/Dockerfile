FROM mageinferno/magento2-php:7.1-fpm-0

MAINTAINER fubolg <fubolg.ua@gmail.com>
LABEL Vendor="fubolg"
LABEL Description="PHP-FPM v7.1"
LABEL Version="1.0.0"

ADD https://www.dotdeb.org/dotdeb.gpg /tmp/dotdeb.gpg

RUN apt-key add /tmp/dotdeb.gpg \
    && echo "deb http://packages.dotdeb.org jessie all" > /etc/apt/sources.list.d/dotdeb.list \
    && echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list.d/dotdeb.list

RUN apt-get update -y

RUN apt-get install -yqq \
    vim

RUN yes | pecl install xdebug-2.5.0 \
    && docker-php-ext-enable xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_enable=on\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_autostart=on\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.idekey=PHPSTORM\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_port=9001\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_host=localhost\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_enable=0\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=on\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini