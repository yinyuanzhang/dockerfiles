
FROM ubuntu
MAINTAINER "Mattias Hemmingsson" <matte.hemmingsson@gmail.com>




RUN apt-get update &&  apt-get install nginx -y
RUN mkdir -p /home/nginx/localhost/public
RUN chgrp www-data /home/nginx/localhost/public
RUN apt-get update && apt-get install php-fpm php-pgsql php-curl unzip php-gd php-xmlrpc wget php-mysql php-xml php-zip php-mbstring php-soap php-intl vim postfix gettext php-memcached php-redis -y

#Install moodle
## Skippimg this an install moodle manual

#RUN mkdir -p /var/www/html/
#WORKDIR /var/www/html
#RUN wget  https://download.moodle.org/download.php/direct/stable35/moodle-latest-35.tgz
#RUN tar zxvf moodle-latest-35.tgz
#RUN rm moodle-latest-35.tgz

#Install themea 
#WORKDIR /var/www/html/moodle/theme
#RUN wget https://moodle.org/plugins/download.php/16170/theme_adaptable_moodle34_2018022500.zip
#RUN unzip theme_adaptable_moodle34_2018022500.zip
#RUN rm theme_adaptable_moodle34_2018022500.zip

#RUN wget https://moodle.org/plugins/download.php/15563/theme_snap_moodle33_2017063005.zip
#RUN unzip theme_snap_moodle33_2017063005.zip
#RUN rm theme_snap_moodle33_2017063005.zip



#Copy in our own moodle
COPY moodle/ /var/www/html/moodle


#Install language pack
WORKDIR /var/www/html/moodle/lang
RUN wget https://download.moodle.org/download.php/direct/langpack/2.0/sv.zip
RUN unzip sv.zip
RUN rm sv.zip

#Setup php
ADD php.ini /etc/php/7.0/fpm/php.ini


#Setup Moodle
WORKDIR /var/www/html
RUN chmod -R 0755 moodle
RUN mkdir /run/php

#Setup folders
RUN mkdir -p /var/www/html/shared/moodledata
RUN chmod 777 -R /var/www/html/shared/moodledata
RUN mkdir -p /var/www/html/shared/temp
RUN chmod 777 -R /var/www/html/shared/temp
RUN mkdir -p /var/www/html/shared/cache
RUN chmod 777 -R /var/www/html/shared/cache
RUN mkdir -p /var/www/html/local/cache
RUN chmod 777 -R /var/www/html/local/cache


RUN chmod 775 /var/www/html/moodle
RUN chown www-data:www-data -R /var/www/html
ADD config.tpl /config.tpl
RUN chmod 644 /config.tpl
ADD config_no_tls.tpl /config_no_tls.tpl
RUN chmod 644 /config_no_tls.tpl








ADD moodle.conf /etc/nginx/sites-available/default 
ADD nginx.conf /etc/nginx/nginx.conf
ADD start.sh /start.sh
RUN chmod +x /start.sh
CMD /start.sh
