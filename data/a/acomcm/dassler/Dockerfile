FROM ubuntu:latest
MAINTAINER Ivan <ivan.petrus@acommerce.asia>

RUN echo PHP 7.0.9 && apt-get update && apt-get install -y software-properties-common

RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

RUN echo PHP 7.09 && apt-get update && apt-get install -y \
	wget cron curl \
	php7.0-cli php7.0-common php7.0-curl php7.0-fpm php7.0-gd php7.0-mcrypt \
	php7.0-mysql php7.0-pgsql php7.0-sqlite php7.0-readline php7.0-opcache \
	php-ssh2 \
	php7.0-bz2 php7.0-json php7.0-dev supervisor build-essential php-pear git pkg-config libssl-dev libsasl2-dev git && \
	pecl install mongodb && \
	apt-get clean

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    wget -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && \
    chmod 755 /usr/local/bin/composer /usr/local/bin/phpunit

ADD php-fpm.conf /etc/php/7.0/fpm/php-fpm.conf

CMD ["php-fpm7.0", "-F"]
