FROM php:7.2-apache

COPY facturascripts.sh /facturascripts.sh

RUN  apt-get update && \
  apt-get install -y zlib1g-dev libpq-dev wget unzip apt-utils  &&\
  rm -rf /var/lib/apt/lists/* && \
  docker-php-ext-install zip pgsql pdo_pgsql mysqli pdo_mysql


RUN ln -s /var/www/html /facturascripts-home

VOLUME /facturascripts-home

ENTRYPOINT /facturascripts.sh
