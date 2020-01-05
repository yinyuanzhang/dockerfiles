FROM php:7.0.10-fpm-alpine

RUN docker-php-ext-install pdo_mysql ftp mcrypt soap

RUN curl https://getcomposer.org/installer > /tmp/composer.php && \
    php /tmp/composer.php --install-dir=/usr/local/bin --filename=composer && \
    rm -v /tmp/composer.php 
    
RUN composer global require "phpunit/phpunit=5.3.*" && \
    composer global require "hirak/prestissimo:^0.3" && \
    ln -sf /root/.composer/vendor/bin/phpunit /usr/local/bin/phpunit && \
    rm -rfv /root/.composer/cache
