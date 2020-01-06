FROM haklop/nginx-fpm

ADD conf/nginx.conf /etc/nginx/nginx.conf

ADD . /usr/local/nginx/html

WORKDIR /usr/local/nginx/html

RUN apt-get -y install curl git

RUN apt-get -y install couchdb

RUN curl -s http://getcomposer.org/installer | php
RUN php composer.phar install
RUN php composer.phar dumpautoload -o