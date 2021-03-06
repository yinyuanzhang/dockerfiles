FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive

####################################################
###############GENERAL SECTION######################
####################################################

RUN apt-get update && apt-get upgrade -yq

RUN apt-get -yq install apt-utils
RUN apt-get -yq install htop
RUN apt-get -yq install ncdu
RUN apt-get -yq install curl
RUN apt-get -yq install nano
RUN apt-get -yq install wget
RUN apt-get -yq install supervisor

####################################################
##############APACHE SECTION########################
####################################################

RUN apt-get install -yq apache2
RUN a2enmod rewrite 
RUN a2enmod ssl

####################################################
###############PHP SECTION##########################
####################################################

RUN apt-get -yq update
RUN apt-get -yq install php 
RUN apt-get -yq install php-pear 
RUN apt-get -yq install php7.2-dev 
RUN apt-get -yq install php7.2-zip 
RUN apt-get -yq install php7.2-curl 
RUN apt-get -yq install php7.2-gd 
RUN apt-get -yq install php7.2-mysql 
RUN apt-get -yq install php7.2-xml 
RUN apt-get -yq install libapache2-mod-php7.2 
RUN apt-get -yq install php7.2-bcmath 
RUN apt-get -yq install php-imagick

####################################################
###############MYSQL SECTION########################
####################################################

RUN apt-get install -yq lsb-release
RUN apt-get install -yq gnupg
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8C718D3B5072E1F5
RUN wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.10-1_all.deb 
RUN dpkg -i mysql-apt-config_0.8.10-1_all.deb
RUN apt update
RUN apt-get -yq install mysql-server

####################################################
###############GOOGLE MOD PAGESPEED#################
####################################################

RUN wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-stable_current_amd64.deb
RUN dpkg -i mod-pagespeed-*.deb
RUN apt-get -f install
RUN rm mod-pagespeed-*.deb 

####################################################
###############PHPMYADMIN###########################
####################################################

RUN apt-get -fy install phpmyadmin

COPY ./phpmyadmin/phpmyadmin.conf ./etc/apache2/conf-enabled/phpmyadmin.conf
COPY ./phpmyadmin/config.inc.php ./etc/phpmyadmin/config.inc.php

##########################
##########SETUP###########
##########################

ADD /supervisor_conf/supervisor_apache.conf /etc/supervisor/conf.d/supervisor_apache.conf
ADD /supervisor_conf/supervisor_mysql.conf /etc/supervisor/conf.d/supervisor_mysql.conf

COPY ./start.sh ./start.sh
COPY ./helpers/mysql_init.sh ./helpers/mysql_init.sh

COPY ./helpers/mysqld_supervisor.sh ./helpers/mysqld_supervisor.sh
COPY ./helpers/apache2_supervisor.sh ./helpers/apache2_supervisor.sh

COPY ./conf/my.cnf ./etc/my.cnf

EXPOSE 3306 80

RUN mkdir -p cert
RUN chmod 0444 ./etc/my.cnf
RUN chown mysql:mysql ./etc/my.cnf
RUN chmod a+x ./start.sh
RUN chmod a+x ./helpers -R

ENTRYPOINT ["./start.sh"]
