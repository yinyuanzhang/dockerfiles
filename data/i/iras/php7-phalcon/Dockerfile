FROM ubuntu:16.04
MAINTAINER Thomas Flori <tflori@pb-systems.de>

ENV DEBIAN_FRONTEND noninteractive

# fasten up apt
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \
 && echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache

# install php
RUN apt-get update \
 && apt-get install -yq --no-install-recommends \
      php7.0-cli \
      php7.0-cgi \
      php7.0-curl \
      php7.0-gd \
      php7.0-ldap \
      php7.0-mysql \
      php7.0-odbc \
      php7.0-opcache \
      php7.0-pgsql \
      php7.0-readline \
      php7.0-sqlite3 \
      php7.0-tidy \
      php7.0-xml \
      php7.0-bcmath \
      php7.0-bz2 \
      php7.0-imap \
      php7.0-intl \
      php7.0-mbstring \
      php7.0-mcrypt \
      php7.0-soap \
      php7.0-json \
      php7.0-zip \
      php-amqp \
      php-memcached \
      curl \
      ca-certificates \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
 && echo "extension=amqp.so" > /etc/php/7.0/mods-available/amqp.ini \
 && phpenmod amqp

# install phalcon
ADD phalcon-installer.sh /tmp/phalcon-installer.sh
RUN bash /tmp/phalcon-installer.sh
