FROM php:5.6.3-fpm

MAINTAINER neolao <contact@neolao.com>


RUN apt-get update && apt-get install -y wget unzip php5-dev

WORKDIR /root
RUN wget https://github.com/nicolasff/phpredis/archive/2.2.5.zip
RUN unzip 2.2.5.zip


WORKDIR phpredis-2.2.5

RUN phpize
RUN ./configure
RUN make && make install

RUN cp /root/phpredis-2.2.5/modules/redis.so /usr/lib/php5/20131226/
RUN mkdir /etc/php5/conf.d
RUN echo "extension=redis.so" > /etc/php5/conf.d/redis.ini
RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini
