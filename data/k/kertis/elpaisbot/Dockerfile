FROM php:7.1-cli

ENV REFRESHED_AT 2017-04-22

RUN apt-get update \
    && apt-get install zlib1g zlib1g-dev git -y \
    && docker-php-ext-install zip
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
  php composer-setup.php && \
  php -r "unlink('composer-setup.php');" && \
  mv composer.phar /usr/local/bin/composer

ADD . /code
WORKDIR code
RUN composer install

ENTRYPOINT php runBot.php
