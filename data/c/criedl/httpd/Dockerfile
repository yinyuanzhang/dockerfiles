FROM php:7-apache
RUN apt-get update
RUN apt-get -y install vim net-tools supervisor default-libmysqlclient-dev apache2-dev libgd-dev libmcrypt-dev libgd3 libmcrypt4 libpng-dev libfreetype6-dev libjpeg62-turbo-dev libzip-dev pwgen sudo rsync cron
ADD usr/src /usr/src
WORKDIR /usr/src/mod_auth_cookie_mysql2_1.0
RUN make && make install
RUN apt-get -y remove apache2-dev && apt-get -y autoremove \
 && docker-php-ext-configure gd \
 && docker-php-ext-install exif gd pdo_mysql mysqli zip
WORKDIR /
COPY usr/local/sbin /usr/local/sbin
EXPOSE 80/tcp 443/tcp
CMD run.sh
