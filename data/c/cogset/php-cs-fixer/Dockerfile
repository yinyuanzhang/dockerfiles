# PHP Coding Standards Fixer
# Cogset Open Source Group

FROM php:7-alpine

MAINTAINER Cogset <cogset@funcuter.org>

ENV PHP_CS_FIXER_VERSION v2.13.1

RUN curl -L https://github.com/FriendsOfPHP/PHP-CS-Fixer/releases/download/$PHP_CS_FIXER_VERSION/php-cs-fixer.phar -o /usr/local/bin/php-cs-fixer \
    && chmod +x /usr/local/bin/php-cs-fixer

CMD ["/usr/local/bin/php-cs-fixer", "fix"]