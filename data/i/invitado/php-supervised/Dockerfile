FROM php:7.3.11-alpine

# Install needed PHP extensions.
RUN apk add --update libpng-dev && rm -rf /var/cache/apk/*
RUN docker-php-ext-install pdo_mysql sockets bcmath gd

RUN apk add --update --no-cache $PHPIZE_DEPS \
    && pecl install mailparse-3.0.3 \
    && docker-php-ext-enable mailparse \
    && apk del $PHPIZE_DEPS

# Install AMQP extension.
RUN apk add --update --no-cache php7-pecl-amqp \
    && mv /usr/lib/php7/modules/amqp.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/amqp.so \
    && mv /etc/php7/conf.d/40_amqp.ini /usr/local/etc/php/conf.d/40_amqp.ini

# Install S6.
RUN apk add --update s6 && rm -rf /var/cache/apk/*
COPY s6 /opt/s6

# Add entrypoint script.
COPY ./entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["/dev/true"]
