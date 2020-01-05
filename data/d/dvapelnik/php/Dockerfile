FROM        dvapelnik/php:5-fpm

MAINTAINER  Dmitry Vapelnik <dvapelnik@gmail.com>

COPY php.d/xdebug.ini /tmp/xdebug.ini

RUN apt-get update && \
    apt-get install -y libpng12-dev sudo git zip unzip supervisor && \
    docker-php-ext-install pdo pdo_mysql gd && \
    pecl install xdebug && \
    echo "zend_extension=xdebug.so" >> /usr/local/etc/php/conf.d/xdebug.ini && \
    cat /tmp/xdebug.ini >> /usr/local/etc/php/conf.d/xdebug.ini && \
    rm -f /tmp/xdebug.ini && \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');" && \
    apt-get autoremove && \
    apt-get clean
