FROM php:7-alpine

MAINTAINER Toni Van de Voorde "toni.vdv@gmail.com"

ENV PHP_CS_FIXER_VERSION v2.15.5

RUN curl -L https://github.com/FriendsOfPHP/PHP-CS-Fixer/releases/download/${PHP_CS_FIXER_VERSION}/php-cs-fixer.phar -o php-cs-fixer \
    && chmod +x php-cs-fixer \
    && mv php-cs-fixer /usr/local/bin/php-cs-fixer

CMD ["/usr/local/bin/php-cs-fixer", "fix"]
