FROM ubuntu:16.04

MAINTAINER Danil Kopylov <lobsterk@yandex.ru>

# Install.
RUN \
  export LANG=C.UTF-8 && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:ondrej/php && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    nginx \
    php-fpm \
    ca-certificates \
    gettext \
    mc \
    libmcrypt-dev  \
    libicu-dev \
    libcurl4-openssl-dev \
    mysql-client \
    libldap2-dev \
    libfreetype6-dev \
    libfreetype6 \
    libpng12-dev

# exts
RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    php5.6-curl \
    php5.6-intl \
    php5.6-fpm \
    php5.6-soap \
    php5.6-xml \
    php5.6-mcrypt \
    php5.6-bcmath \
    php5.6-mysql \
    php-amqp \
    php5.6-mbstring \
    php5.6-ldap \
    php5.6-zip \
    php5.6-json \
    php5.6-xmlrpc \
    php5.6-gmp \
    php5.6-ldap

# Install git core
RUN apt install -y --no-install-recommends --no-install-suggests \
    git

# Install node.js
RUN apt-get install -y --no-install-recommends --no-install-suggests \
    nodejs \
    npm
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g gulp-cli

RUN apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install mail server
COPY mailserver.sh /tmp/mailserver.sh
RUN /tmp/mailserver.sh

# set timezone Europe/Moscow
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
	&& ln -sf /dev/stderr /var/log/php5.6-fpm.log

RUN rm -f /etc/nginx/sites-enabled/*
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf
#COPY php.ini /etc/php/7.0/fpm/php.ini


RUN mkdir -p /run/php && touch /run/php/php7.0-fpm.sock && touch /run/php/php7.0-fpm.pid
RUN mkdir -p /run/php && touch /run/php/php5.6-fpm.sock && touch /run/php/php5.6-fpm.pid
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
EXPOSE 80
CMD ["/entrypoint.sh"]