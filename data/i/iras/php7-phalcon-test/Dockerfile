FROM iras/php7-phalcon:php7-phalcon-1.0
MAINTAINER Thomas Flori <tflori@pb-systems.de>

ENV DEBIAN_FRONTEND noninteractive

RUN curl -sS http://getcomposer.org/installer | php \
 && mv composer.phar /usr/local/bin/composer \
 && curl -sS https://phar.phpunit.de/phpunit-5.4.6.phar > /usr/local/bin/phpunit \
 && chmod 755 /usr/local/bin/phpunit \
 && apt-get update \
 && apt-get install -yq --no-install-recommends \
      php-xdebug \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
