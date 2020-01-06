FROM php:5.6-apache

MAINTAINER Josia <josia-login@rosskopfs.de>

WORKDIR /root

RUN apt-get update && apt-get install -y wget unzip libpng12-dev libmcrypt-dev

# Extension for joomla
RUN docker-php-ext-install mysqli

#Extensions for phpmyadmin
RUN docker-php-ext-install mbstring gd mcrypt

RUN a2enmod rewrite

ENV TZ "Europe/Berlin"
ENV keydir /var/keys
ENV wwwdir /var/www/html

ADD apache-conf apache-conf
RUN cat apache-conf | tee -a /etc/apache2/apache2.conf

ADD phpmyadmin-conf.php phpmyadmin-conf.php

ADD init.sh /root/init.sh
RUN chmod +x init.sh

CMD ["bash", "init.sh"]
