FROM ubuntu:18.04
MAINTAINER Yassine El Garras <yassine7500@gmail.com>
LABEL Description="LAMP stack based on Ubuntu 18.04. Includes PHP 7.3"

# update and upgrade the system
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install software-properties-common -y

#set env var DEBIAN_FRONTEND to avoid user interaction while installing tz
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM dumb
ENV TIMEZONE UTC
ENV APACHE_LOG_LEVEL debug

#add repositories
RUN add-apt-repository ppa:ondrej/php

#install apache and run ap
RUN apt-get install apache2 apache2-utils libapache2-mod-php -y

#install mariadb
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
RUN add-apt-repository 'deb [arch=amd64] http://mirror.zol.co.zw/mariadb/repo/10.3/ubuntu bionic main'
RUN apt update
RUN apt-get install mariadb-server mariadb-client mariadb-common -y

#install pghp 7.3
RUN apt-get update
RUN apt-get install -y \
        php7.3 \
        php7.3-cli \
        php7.3-fpm \
        php7.3-json \
        php7.3-pdo \
        php7.3-mysql \
        php7.3-zip \
        php7.3-gd \
        php7.3-mbstring \
        php7.3-curl \
        php7.3-xml \
        php7.3-bcmath \
        php7.3-json

#app volumes
VOLUME /var/www/html

#mysql lib volumes
VOLUME /var/lib/mysql

#log volumes
VOLUME /var/log/apache2
VOLUME /var/log/mysql

#apache conf volumes
VOLUME /etc/apache2/conf-enabled
VOLUME /etc/apache2/sites-enabled

#enable mod rewrite
RUN a2enmod rewrite

#copy bash script to the image and make it executable
COPY run.sh /usr/sbin/
RUN chmod +x /usr/sbin/run.sh

#change own to apache on the http volume
RUN chown -R www-data:www-data /var/www/html

#grant access to databse from any host
RUN echo "[mysqld]" >> /etc/mysql/my.cnf
RUN echo "bind-address=0.0.0.0" >> /etc/mysql/my.cnf
RUN chown -R mysql:mysql /var/lib/mysql
#RUN mysql_install_db --user=mysql --ldata=/var/lib/mysql

#expose ports 80 & 443 for apache and 3360 for mysql
EXPOSE 80
EXPOSE 443
EXPOSE 3306

CMD ["/usr/sbin/run.sh"]
