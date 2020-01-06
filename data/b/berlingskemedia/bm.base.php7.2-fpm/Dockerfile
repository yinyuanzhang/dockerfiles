FROM php:7.2-fpm-alpine

RUN apk --no-cache add pcre-dev ${PHPIZE_DEPS} \
  && pecl install apcu \
  && docker-php-ext-enable apcu \
  && apk del pcre-dev ${PHPIZE_DEPS}

RUN apk add --update \
    php7-curl \
    php7-iconv \
    php7-json \
    php7-intl \
    php7-mcrypt \
    php7-mbstring \
    php7-opcache \
    php7-openssl \
    php7-pdo \
    php7-session

RUN rm -rf /tmp/* /var/cache/apk/*

# PHP config
ADD php-fpm.conf /etc/php/7.2/fpm/php-fpm.conf
ADD www.conf /etc/php/7.2/fpm/pool.d/www.conf

# Define default command.
CMD ["php-fpm"]