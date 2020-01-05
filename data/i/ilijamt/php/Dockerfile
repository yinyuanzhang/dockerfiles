FROM debian:jessie

MAINTAINER Ilija Matoski <ilijamt@gmail.com>

# Install base thingies
RUN set -x \
    && apt-get update \
    && apt-get install -y wget curl build-essential apt-transport-https lsb-release ca-certificates \
    && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb https://packages.sury.org/php/ jessie main" > /etc/apt/sources.list.d/php.list

# Install base required applications
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
		php7.0 \
		php7.0-fpm \
		php7.0-redis \
		php7.0-common \
		php7.0-cli \
		php7.0-apcu \
		php7.0-intl \
		php7.0-mcrypt \
		php7.0-mongo \
		php7.0-dev \
		php7.0-mysqlnd \
		php7.0-readline \
		php7.0-msgpack \
		php7.0-json \
		php7.0-gd \
		php7.0-imagick \
		php7.0-igbinary \
		php-pear \
    && apt-get clean -y \
    && apt-get autoclean -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Setup PHP
RUN echo "date.timezone = UTC" > /etc/php/7.0/mods-available/timezone.ini \
    && cd /etc/php/7.0/cli/conf.d && ln -s ../../mods-available/timezone.ini 01-timezone.ini \
    && cd /etc/php/7.0/fpm/conf.d && ln -s ../../mods-available/timezone.ini 01-timezone.ini
