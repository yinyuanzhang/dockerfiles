# Install on an Alpine Linux: Git, Wget, PHP7 with extensions and Composer
FROM composer/composer:alpine

MAINTAINER Louis Lagrange <lagrange.louis+docker@gmail.com>

# Add repository needed for php7-pear
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories

## Install nodejs and PHP extensions
RUN apk --no-cache add \
    nodejs \
    build-base \
    gmp-dev \
    php7-pear

ADD php.ini /usr/local/etc/php/

RUN docker-php-ext-install gmp \
  && docker-php-ext-install pdo_mysql \
  && docker-php-ext-install intl

# Install NodeJS tools
RUN npm install -g bower \
  && npm install -g gulp-cli

# Install phpunit
RUN wget https://phar.phpunit.de/phpunit.phar \
  && chmod +x phpunit.phar \
  && mv phpunit.phar /usr/local/bin/phpunit

# Reset entrypoint
ENTRYPOINT []
