FROM php:7-zts-alpine

RUN apk --no-cache --update add \
    icu-dev \
	bash git openssh \
    && docker-php-ext-install intl
