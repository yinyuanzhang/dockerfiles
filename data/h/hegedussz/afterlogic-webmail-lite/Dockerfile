FROM ubuntu:18.04
MAINTAINER AfterLogic Support <support@afterlogic.com>, Szabolcs Hegedus <szabolcs.hegedus@gmail.com>

# installing packages and dependencies
ENV DEBIAN_FRONTEND noninteractive 
ENV TZ=Europe/Budapest
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get -y install \
     wget \
     unzip \
     iputils-ping \
     supervisor \
     apache2 \
     libapache2-mod-php \
     php7.3 \
     php7.3-common \
     php7.3-curl \
     php7.3-fpm \
     php7.3-cli \
     php7.3-mysqlnd \
     php7.3-dev \
     php7.3-mbstring \
     libmcrypt-dev \
     php-pear \
     htop \
     mc \
     nano \
     nload \
     ncdu 

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# adding configuration files and scripts
ADD files/start-apache2.sh /start-apache2.sh
ADD files/run.sh /run.sh
ADD files/supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
RUN chmod 755 /*.sh


# setting up default apache config
ADD files/apache.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite
RUN a2enmod remoteip
# Setting IP remote

RUN echo "RemoteIPHeader X-Forwarded-For" >> /etc/apache2/conf-available/remoteip.conf
RUN echo "RemoteIPTrustedProxy 10.0.0.0/8" >> /etc/apache2/conf-available/remoteip.conf
COPY files/apache2.conf /etc/apache2/apache2.conf
RUN ln -s  /etc/apache2/conf-available/remoteip.conf  /etc/apache2/conf-enabled/remoteip.conf

# downloading and setting up webmail
RUN rm -rf /tmp/alwm
RUN mkdir -p /tmp/alwm
RUN wget -P /tmp/alwm https://afterlogic.org/download/webmail_php.zip
RUN unzip -q /tmp/alwm/webmail_php.zip -d /tmp/alwm/webmail/
RUN rm -rf /var/www/html
RUN mkdir -p /var/www/html
RUN cp -r /tmp/alwm/webmail/* /var/www/html
RUN rm -rf /var/www/html/install
RUN chown www-data.www-data -R /var/www/html
COPY files/config.json /var/www/html/data/settings/config.json
RUN rm -rf /tmp/alwm
RUN chmod 0777 -R /var/www/html/data

# setting php configuration values
ENV PHP_UPLOAD_MAX_FILESIZE 128M
ENV PHP_POST_MAX_SIZE 128M

RUN service apache2 start

# adding mysql volumes
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]


EXPOSE 80 3306
CMD ["/run.sh"]
