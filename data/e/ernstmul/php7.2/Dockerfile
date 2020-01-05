FROM php:7.3-cli-alpine

RUN apk add --update --no-cache autoconf g++ imagemagick-dev libtool make pcre-dev zip imagemagick git openssh-client \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer global require "hirak/prestissimo:^0.3" --prefer-dist --no-progress --no-suggest --classmap-authoritative \
    && curl -L https://deployer.org/deployer.phar > /usr/local/bin/deployer \
    && chmod +x /usr/local/bin/deployer



