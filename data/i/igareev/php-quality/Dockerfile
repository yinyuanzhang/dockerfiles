FROM php:7.2-alpine

RUN apk add --update openssh-client bash wget curl git

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN wget http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar -O /usr/local/bin/php-cs \
	&& chmod +x /usr/local/bin/php-cs \
    && wget https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -O /usr/local/bin/php-snif \
	&& chmod +x /usr/local/bin/php-snif \
    && wget -O /usr/local/bin/phpstan https://github.com/phpstan/phpstan-shim/raw/0.11/phpstan.phar \
	&& chmod +x /usr/local/bin/phpstan
WORKDIR /app

LABEL maintainer "Radik Ilin <andmetoo@mail.ru"

LABEL version="1.0.3"
