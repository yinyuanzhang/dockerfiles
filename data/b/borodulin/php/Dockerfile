FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y software-properties-common

RUN apt-get install -y language-pack-en-base

RUN apt-get install -y iputils-ping

RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php


RUN echo "Europe/Moscow" > /etc/timezone
RUN apt-get install tzdata -y
RUN dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install -y php7.2 php7.2-cli php7.2-common php7.2-json php7.2-opcache php7.2-mysql php7.2-mbstring \
    php7.2-zip php7.2-fpm php7.2-dev php7.2-pgsql php7.2-amqp php7.2-xml php7.2-intl php7.2-curl php7.2-bcmath \
    php7.2-gd php7.2-imagick php7.2-igbinary

RUN pecl install timezonedb \
    && echo "extension=timezonedb.so" > /etc/php/7.2/mods-available/timezonedb.ini \
    && phpenmod timezonedb

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

RUN apt-get install -y git

RUN  apt-get install -y supervisor

RUN mkdir /run/php

WORKDIR /app

EXPOSE 9000

RUN echo "listen = 0.0.0.0:9000" >> /etc/php/7.2/fpm/pool.d/www.conf

CMD ["php-fpm7.2", "--nodaemonize"]

