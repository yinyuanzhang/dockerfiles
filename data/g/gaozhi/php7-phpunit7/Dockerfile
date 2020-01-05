FROM php:7-alpine as installer

RUN apk add --update --no-cache --virtual .ext-deps \
        icu-dev

RUN docker-php-ext-configure intl && \
    docker-php-ext-install intl

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php
RUN wget -O phpunit https://phar.phpunit.de/phpunit-7.phar

FROM php:7-alpine
COPY --from=installer /usr/local/lib/php/extensions/no-debug-non-zts-20170718/* /usr/local/lib/php/extensions/no-debug-non-zts-20170718/
COPY --from=installer /composer.phar /usr/local/bin/composer
COPY --from=installer /phpunit /usr/local/bin/phpunit

RUN chmod +x /usr/local/bin/composer /usr/local/bin/phpunit
RUN apk add --update --no-cache --virtual .ext-deps \
        icu-dev

RUN docker-php-ext-enable intl