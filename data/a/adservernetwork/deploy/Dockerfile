FROM ubuntu:18.04

MAINTAINER adserver.network

ENV PHP_VERSION 7.2

ENV GEOIP_LIB_DIR /usr/local/share/GeoIP
ENV PHP_INI_PATH /etc/php/${PHP_VERSION}/mods-available
ENV PHP_FPM_CONF_PATH /etc/php/${PHP_VERSION}/fpm/conf.d

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y software-properties-common

ENV TZ 'Europe/Kiev'

RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

RUN apt-get install -y --force-yes \
  php7.2 \
  php7.2-mysql \
  php7.2-ldap \
  php7.2-xmlrpc \
  php7.2-curl \
  php7.2-gd \
  php7.2-mbstring \
  php7.2-simplexml \
  php7.2-xml \
  php7.2-apcu \
  php7.2-imap \
  php7.2-fpm \
  php7.2-intl \
  php7.2-gmp \
  php7.2-bcmath \
  php7.2-opcache \
  php-dev \
  php-pear \
  php-cas \
  php-gettext \
  libevent-dev \
  libyaml-dev \
  composer \
  openssh-client \
  vim \
  wget \
  curl \
  git \
  unzip \
  supervisor \
  apt-utils \
  procps \
  rsync \
  openssl \
  openssh-client \
  libmcrypt-dev \
  libz-dev \
  libmemcached-dev \
  mc \
  gnupg2 \
  pkg-config \
  mysql-client \
  tar \
  python-pip

RUN pecl install nsq
RUN pecl install redis
RUN pecl install yaml

RUN add-apt-repository ppa:longsleep/golang-backports

RUN apt install -y --force-yes \
    golang-go

RUN pip install ansible-tower-cli
RUN pip install six
RUN pip install idna

COPY php-fpm.ini /etc/php/7.2/fpm/php.ini

COPY php-php.ini /etc/php/7.2/cli/php.ini

COPY /supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN set -xe \
    && command -v composer \
    && composer global require hirak/prestissimo \
    && composer global require laravel/laravel \
    && : "---------- Install PHPUnit -----------\n" \
    && wget https://phar.phpunit.de/phpunit.phar \
    && chmod +x phpunit.phar \
    && mv phpunit.phar /usr/local/bin/phpunit \
    && command -v phpunit\
    && : "--------- Node.js -------------\n" \
    && curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt-get install nodejs -y \
    && command -v node \
    && command -v npm \
    && npm -g i npm \
    && npm -g i @coreui/coreui-pro@^2.1.1 \
    && npm -g i @coreui/react@^2.1.1 \
    && npm -g i @coreui/icons@^0.3.0 \
    && npm -g i axios@^0.18.0 \
    && npm -g i bootstrap@^4.3.1 \
    && npm -g i chart.js@^2.7.3 \
    && npm -g i classnames@^2.2.6 \
    && npm -g i core-js@^2.6.5 \
    && : "---------- apt purge -----------\n" \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && : "---------- finish -----------\n" \
    && mkdir /builds

COPY GeoIP2-City.mmdb ${GEOIP_LIB_DIR}/GeoIP2-City.mmdb
COPY GeoIP2-Country.mmdb ${GEOIP_LIB_DIR}/GeoIP2-Country.mmdb

WORKDIR /builds

EXPOSE 9000

CMD ["/usr/bin/supervisord"]
