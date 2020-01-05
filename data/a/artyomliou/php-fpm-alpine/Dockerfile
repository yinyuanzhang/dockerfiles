ARG PHP_VERSION=7.2

FROM php:${PHP_VERSION}-fpm-alpine

LABEL maintainer="ArtyomLiou <artyomliou@gmail.com>"

ARG PHP_VERSION=7.2

#
#--------------------------------------------------------------------------
# Optional Software's Installation
#--------------------------------------------------------------------------
#
# Optional Software's will only be installed if you set them to `true`
# in the `docker-compose.yml` before the build.
# Example:
#   - INSTALL_SOAP=true
#


# RUN printf "\n" | pecl install -o -f redis \
#     &&  rm -rf /tmp/pear \
#     &&  docker-php-ext-enable redis \
#     &&  docker-php-ext-install pcntl bcmath opcache mysqli pdo_mysql \
#     &&  docker-php-ext-configure gd \
#           --with-jpeg-dir=/usr/lib \
#           --with-freetype-dir=/usr/include/freetype2 \
#     &&  docker-php-ext-install gd

RUN docker-php-ext-install bcmath pdo_mysql pcntl && \
    docker-php-source delete


# Check PHP version:
RUN set -xe; php -v | head -n 1 | grep -q "PHP ${PHP_VERSION}."


# Final Touch
COPY ./opcache.ini /usr/local/etc/php/conf.d/opcache.ini
COPY ./laravel.ini /usr/local/etc/php/conf.d
COPY ./xlaravel.pool.conf /usr/local/etc/php-fpm.d/
COPY ./php7.2.ini /usr/local/etc/php/php.ini


WORKDIR /var/www

CMD ["php-fpm"]

EXPOSE 9000
