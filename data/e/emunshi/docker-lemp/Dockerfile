# nginx + PHP5-FPM + MariaDB + supervisord on Docker
#
# VERSION               0.0.1
FROM emunshi/ubuntu

MAINTAINER Tarun Gupta "emunshi.studio@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

#add user and group
RUN groupadd www && useradd -g www www

# Update packages
# RUN apt-key update
RUN apt-get update

# install curl, wget
RUN apt-get install -y curl wget software-properties-common

RUN locale-gen en_US.UTF-8
RUN export LANG=en_US.UTF-8

# install keyring
#RUN apt-get install -y debian-archive-keyring debian-keyring

# Configure repos
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db 
RUN add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/10.1/ubuntu trusty main'
RUN add-apt-repository -y ppa:nginx/stable
RUN add-apt-repository -y ppa:ondrej/php5
RUN apt-get update

# Install MariaDB
RUN apt-get -y install mariadb-server
#RUN sed -i 's/^innodb_flush_method/#innodb_flush_method/' /etc/mysql/my.cnf

# Install nginx
RUN apt-get -y --force-yes install nginx

# Install PHP5 and modules
RUN apt-get -y  --force-yes install php5-fpm php5-mysql php-apc php5-imap php5-mcrypt php5-curl php5-gd php5-json

# Configure nginx for PHP websites
ADD nginx_default.conf /etc/nginx/sites-available/default
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini
RUN mkdir -p /var/www && chown -R www:www /var/www && echo "<?php phpinfo(); ?>" >> /var/www/index.php

# install composer and phpunit 
#RUN curl -sS https://getcomposer.org/installer | php && \
#	mv composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer && \
#	composer global require 'phpunit/phpunit=3.7.*' && \
#	echo "export PATH=$PATH:/.composer/vendor/bin/:" >> /root/.profile && \
#  echo "export PATH=$PATH:/.composer/vendor/bin/:" >> /home/www/.profile

# Supervisord
RUN apt-get -y install python-setuptools
RUN easy_install supervisor
ADD supervisord.conf /etc/supervisord.conf

EXPOSE 80

CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
