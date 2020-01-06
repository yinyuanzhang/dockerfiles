FROM php:7.1

RUN apt-get update -yqq
RUN apt-get install apt-utils -y
RUN apt-get install git -yqq
RUN apt-get install -y zlib1g-dev libfreetype6-dev libjpeg62-turbo-dev libpng12-dev libxpm-dev libvpx-dev libmcrypt-dev libgmp-dev
RUN apt-get install wget -y
RUN wget http://xdebug.org/files/xdebug-2.5.0.tgz
RUN tar -xzf xdebug-2.5.0.tgz && cd xdebug-2.5.0 && phpize && ./configure --enable-xdebug && make && cp modules/xdebug.so /usr/lib/. && php --ini

RUN docker-php-ext-configure gd \
     --with-freetype-dir=/usr/lib/x86_64-linux-gnu/ \
     --with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ \ 
     --with-xpm-dir=/usr/lib/x86_64-linux-gnu/  \
     --with-vpx-dir=/usr/lib/x86_64-linux-gnu/ 

RUN docker-php-ext-install pdo pdo_mysql mysqli opcache zip gd

RUN curl -sS https://getcomposer.org/installer| php


RUN echo 'zend_extension="/usr/lib/xdebug.so"'> /usr/local/etc/php/conf.d/20-xdebug.ini
RUN echo 'xdebug.remote_enabled=1' >> /usr/local/etc/php/conf.d/20-xdebug.ini

RUN wget https://phar.phpunit.de/phpunit-6.0.phar && chmod +x phpunit-6.0.phar && mv phpunit-6.0.phar /usr/local/bin/phpunit



