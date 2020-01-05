FROM php:7.3-fpm-alpine as php

WORKDIR /var/www/html

# Installing required dependencies
RUN apk --no-cache add $PHPIZE_DEPS imagemagick imagemagick-dev mariadb-client jpegoptim optipng gifsicle icu-dev bzip2-dev libzip-dev zip supervisor shadow \
        # Install dependancies
        && docker-php-ext-configure zip --with-libzip > /dev/null \
        && docker-php-ext-install -j$(nproc) pdo_mysql intl zip bz2 opcache exif bcmath pcntl > /dev/null \
        && pecl install -o -f redis > /dev/null \
        && pecl install -o -f imagick > /dev/null \
        && docker-php-ext-enable redis \
        && docker-php-ext-enable imagick \
        # Change group and user id
        && groupmod -g 1000 www-data \
        && usermod -u 1000 www-data \
        # Allow www-data group to read php config files
        && chown root:www-data -R /usr/local/etc/php \
        && chmod g+r -R /usr/local/etc/php \
        && chown -R www-data:www-data /var/www/html \
        # Cleanup
        && apk del $PHPIZE_DEPS shadow \
        && rm -rf /tmp/* /usr/local/lib/php/doc/* /var/cache/apk/* \
        && rm -rf /tmp/pear ~/.pearrc