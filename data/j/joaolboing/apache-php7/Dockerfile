FROM joaolboing/apache:16.04

MAINTAINER joaolboing <joaolboing@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
apt-get install -y php7.0 \
libapache2-mod-php7.0 \
php7.0-xml \
php7.0-xmlrpc \
php7.0-fpm \
php7.0-cli \
php7.0-curl \
php7.0-gd \
php7.0-mcrypt \
php-apcu \
php7.0-json \
php7.0-pgsql \
php7.0-zip \
php7.0-mbstring \
php-soap && \

phpenmod mcrypt && \

sed -i 's/^display_errors = .*/display_errors = On/' /etc/php/7.0/apache2/php.ini && \
sed -i 's/^error_reporting = .*/error_reporting = E_ALL \& ~E_DEPRECATED \& ~E_STRICT \& ~E_NOTICE/' /etc/php/7.0/apache2/php.ini && \


rm -rf /var/lib/apt/lists/*
