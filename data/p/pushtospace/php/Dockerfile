FROM php:7.2-fpm

MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>

# Base image updates
RUN apt-get update && apt-get upgrade -y && apt-get install automake git wget libmcrypt-dev unzip libfreetype6-dev libjpeg62-turbo-dev libpng-dev libbz2-dev libtool libmosquitto-dev -y && apt-get clean
# Ext installation
RUN pecl install mcrypt-1.0.1 && docker-php-ext-enable mcrypt
RUN docker-php-ext-install pdo pdo_mysql iconv mbstring mysqli bcmath && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && docker-php-ext-install gd bz2 zip

# NgHttp2 installation
RUN git clone https://github.com/tatsuhiro-t/nghttp2 && cd nghttp2 && autoreconf -i && automake && autoconf && ./configure --prefix=/usr && make && make install && cd .. && rm -rf nghttp2

# Redis installation
RUN wget https://github.com/phpredis/phpredis/archive/4.2.0.zip && unzip 4.2.0.zip && cd phpredis-4.2.0 && /usr/local/bin/phpize && ./configure --with-php-config=/usr/local/bin/php-config && make && make install && \
cd .. && rm -rf phpredis-4.2.0 4.2.0.zip

# imap
RUN apt-get install libc-client-dev libkrb5-dev -y && docker-php-ext-configure imap --with-kerberos --with-imap-ssl && docker-php-ext-install imap

ADD ./php.ini /usr/local/etc/php
ADD ./start.sh /root

# Mosquitto installation
RUN pecl install Mosquitto-alpha && chmod +x /root/start.sh

EXPOSE 9000

CMD ["/root/start.sh"]