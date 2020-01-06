FROM ubuntu:latest
MAINTAINER Ivan <ivan@marsud.id>

RUN apt-get update && apt-get install -y software-properties-common

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

RUN add-apt-repository -y ppa:ondrej/php5-5.6

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

RUN echo PHP 5.6.21 && apt-get update && apt-get install -y \
	php5-cli php5-common php5-curl php5-fpm php5-gd php5-mcrypt php5-mysql php5-pgsql php5-sqlite php5-readline \
	php5-xdebug php5-mongo php5-dev build-essential pkg-config libssl-dev libsasl2-dev git supervisor wget && \
	pecl install mongodb && \
  apt-get clean

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    wget -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && \
    chmod 755 /usr/local/bin/composer /usr/local/bin/phpunit

ADD php-fpm.conf /etc/php5/fpm/php-fpm.conf

CMD ["php5-fpm", "-F"]
