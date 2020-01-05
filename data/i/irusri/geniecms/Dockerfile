FROM phusion/baseimage
MAINTAINER Chanaka Mannapperuma <irusri@gmail.com>
ENV REFRESHED_AT 2018-08-21

# based on dgraziotin/lamp
# MAINTAINER Daniel Graziotin <daniel@ineed.coffee>

ENV DOCKER_USER_ID 501 
ENV DOCKER_USER_GID 20

ENV BOOT2DOCKER_ID 1000
ENV BOOT2DOCKER_GID 50

# Tweaks to give Apache/PHP write permissions to the app
RUN usermod -u ${BOOT2DOCKER_ID} www-data && \
    usermod -G staff www-data && \
    useradd -r mysql && \
    usermod -G staff mysql

RUN groupmod -g $(($BOOT2DOCKER_GID + 10000)) $(getent group $BOOT2DOCKER_GID | cut -d: -f1)
RUN groupmod -g ${BOOT2DOCKER_GID} staff

# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN add-apt-repository -y ppa:ondrej/php && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get -y install supervisor wget git apache2 php-xdebug libapache2-mod-php mysql-server php-mysql pwgen php-apcu php7.0-mcrypt php-gd php-xml php-mbstring php-gettext zip unzip php-zip curl php-curl task-spooler amap-align bedtools bioperl bioperl-run gbrowse cmake libncbi6 && \
  apt-get -y autoremove && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

# needed for phpMyAdmin
RUN phpenmod mcrypt

# Add image configuration and scripts
ADD supporting_files/start-apache2.sh /start-apache2.sh
ADD supporting_files/start-mysqld.sh /start-mysqld.sh
ADD supporting_files/run.sh /run.sh
ADD supporting_files/blastall /usr/bin/
ADD supporting_files/formatdb /usr/bin/
ADD supporting_files/fastacmd /usr/bin/
RUN chmod 755 /*.sh
ADD supporting_files/supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
ADD supporting_files/supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf
ADD supporting_files/mysqld_innodb.cnf /etc/mysql/conf.d/mysqld_innodb.cnf
ADD supporting_files/my.cnf /etc/mysql/my.cnf

# Allow mysql to bind on 0.0.0.0
RUN sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/my.cnf
#RUN sed -i "s/.*port.*/port = 3306/" /etc/mysql/my.cnf

# Set PHP timezones to Europe/London
RUN sed -i "s/;date.timezone =/date.timezone = Europe\/London/g" /etc/php/7.2/apache2/php.ini
RUN sed -i "s/;date.timezone =/date.timezone = Europe\/London/g" /etc/php/7.2/cli/php.ini

# Remove pre-installed database
RUN rm -rf /var/lib/mysql

# Add MySQL utils
ADD supporting_files/create_mysql_users.sh /create_mysql_users.sh
RUN chmod 755 /*.sh

# Add phpmyadmin
ENV PHPMYADMIN_VERSION=4.8.2
RUN wget -O /tmp/phpmyadmin.tar.gz https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages.tar.gz
RUN tar xfvz /tmp/phpmyadmin.tar.gz -C /var/www
RUN ln -s /var/www/phpMyAdmin-${PHPMYADMIN_VERSION}-all-languages /var/www/phpmyadmin
RUN mv /var/www/phpmyadmin/config.sample.inc.php /var/www/phpmyadmin/config.inc.php


# Add composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

ENV MYSQL_PASS:-$(pwgen -s 12 1)
# config to enable .htaccess
ADD supporting_files/apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Configure /app folder with sample app
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html
#ADD geniecms/ /app

# Add GenIE-CMS
#ADD https://github.com/irusri/GenIECMS/archive/master.zip .
#RUN unzip master.zip
#RUN mv GenIECMS-master/* /app && rm master.zip

#Environment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M

# Add volumes for the app and MySql
VOLUME  ["/etc/mysql", "/var/lib/mysql", "/app" ]

EXPOSE 80 3306
CMD ["/run.sh"]

#To BUILD
#docker-lamp$ docker build -t genie -f ./Dockerfile  .
#TO RUN 
#docker-lamp$ docker run -d -p "80:80"  -v ${PWD}/geniecms:/app genie
#TO REMOVE ALL CONTAINERS
#docker-lamp$ docker rm -f $(docker ps -a -q)
#TO See/Remove all volumes respectively
#docker-lamp$ docker volume ls/prune
# Delete every Docker images
#docker rmi -f $(docker images -q)

#Running docker interactively with exposing mysql and webserver ports
#docker run --rm -i -t -p "80:80" -p "3308:3306" -v ${PWD}/geniecms:/app  -v ${PWD}/mysql:/var/lib/mysql  -e MYSQL_ADMIN_PASS="mypass" --name geniecms genie

# To stop mysql I used
#mysqld stop or
#killall mysqld
#To start mysql
#mysqld start or sh start-mysqld.sh it has exec mysqld_safe
#It is important to change /etc/mysql/my.inf with bind ip address(0.0.0.0) and the port(3306)

#Last time test
#docker rm -f $(docker ps -a -q)
#docker rmi -f $(docker images -q)
#docker build -t genie2 -f ./Dockerfile  .
#docker run --rm -i -t -p "80:80" -p "3308:3306" -v ${PWD}/geniecms:/app  -v ${PWD}/mysql:/var/lib/mysql -e MYSQL_ADMIN_PASS="mypass" --name geniecms genie2
