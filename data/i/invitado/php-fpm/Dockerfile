FROM php:7.3.11-fpm-alpine

# Install needed PHP extensions.
RUN apk add --update libzip-dev libpng-dev libjpeg-turbo-dev && rm -rf /var/cache/apk/*
RUN docker-php-ext-configure gd --with-gd --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install pdo_mysql sockets opcache bcmath gd zip

# Install ImageMagick extension
RUN set -ex \
    && apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS imagemagick-dev libtool \
    && export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS" \
    && pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick \
    && apk add --no-cache --virtual .imagick-runtime-deps imagemagick \
    && apk del .phpize-deps

# Install MailParse package.
RUN apk add --update --no-cache $PHPIZE_DEPS \
    && pecl install mailparse-3.0.3 \
    && docker-php-ext-enable mailparse \
    && apk del $PHPIZE_DEPS

# Install AMQP extension.
RUN apk add --update --no-cache php7-pecl-amqp \
    && mv /usr/lib/php7/modules/amqp.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/amqp.so \
    && mv /etc/php7/conf.d/40_amqp.ini /usr/local/etc/php/conf.d/40_amqp.ini

# Install dumb init.
RUN apk add --update dumb-init && rm -rf /var/cache/apk/*

# Add necessary configuration files.
RUN rm -rf /usr/local/etc/php-fpm.d/*
COPY ./php-fpm.conf /usr/local/etc/php-fpm.d/php-fpm.conf

# Add entrypoint script.
COPY ./entrypoint.sh /opt/entrypoint.sh
RUN chmod 755 /opt/entrypoint.sh
CMD ["/opt/entrypoint.sh"]
