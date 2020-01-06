FROM php:7.1-fpm

RUN apt-get update && apt-get install -y libmcrypt-dev mysql-client zip git \
    && docker-php-ext-install mcrypt pdo_mysql mbstring

# Install composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php --install-dir=/bin && \
    php -r "unlink('composer-setup.php');"

WORKDIR /var/www

RUN ln -sf /dev/stderr /var/log/fpm-access.log
RUN ln -sf /dev/stderr /var/log/fpm-error.log

RUN export TERM=xterm

