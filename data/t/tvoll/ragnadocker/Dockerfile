       FROM ubuntu:latest 
 MAINTAINER Tyler Voll <tylervollbooks@gmail.com>
        ENV DEBIAN_FRONTEND noninteractive
       USER root
        ENV HOME /root
        ADD boottime.sh /
        ADD import.sql /
        ADD 000-default.conf /
        ADD my.cnf /
        ADD launch-athena.sh /
        ADD reset-athena.sh /
        ADD backup-athena.sh /
        ADD import-athena.sh /
    WORKDIR /usr/bin/rathena/		
        RUN apt-get update \
         && mkdir /datastore/ \
         && mkdir /datastore/etc-apache2/ \
         && mkdir /datastore/etc-mysql/ \
         && mkdir /datastore/usr-bin-rathena/ \
         && mkdir /datastore/var-lib-mysql/ \
         && mkdir /datastore/var-www-html/ \
         && mkdir /datastoresetup/ \
         && mkdir /datastoresetup/etc-apache2/ \
         && mkdir /datastoresetup/etc-mysql/ \
         && mkdir /datastoresetup/usr-bin-rathena/ \
         && mkdir /datastoresetup/var-lib-mysql/ \
         && mkdir /datastoresetup/var-www-html/ \
         && apt-get -yqq dist-upgrade \
         && apt-get -yqq --force-yes install apache2 \
                                             g++ \
                                             git \
                                             libapache2-mod-php7.2 \
                                             libmysqlclient-dev \
                                             libpcre3-dev \
                                             make \
                                             mysql-client \
                                             mysql-server \
                                             php7.2-mysql \
                                             php-apcu \
                                             php7.2 \
                                             rsync \
                                             zlib1g-dev \
         && echo "ServerName localhost" >> /etc/apache2/apache2.conf \
         && rm -rf /var/www/html \
         && git clone https://github.com/rathena/FluxCP.git /var/www/html/fluxcp \
         && git clone https://github.com/rathena/rathena.git /usr/bin/rathena \
         && ./configure --enable-packetver=20151104 \
         && make server \
         && service mysql start \
         && mysql < /import.sql \
         && service mysql stop \
         && apt-get -yqq remove gcc git make \
         && apt-get -yqq autoremove \
         && chmod a+x /usr/bin/rathena/*-server \
         && chmod a+x /usr/bin/rathena/athena-start \
         && chmod a+x /*.sh \
         && chmod -R 777 /var/www/html/fluxcp/data \
         && chown -R 33:33 /var/www/html/fluxcp/data \
         && chmod -R 777 /datastore \
         && chown -R 33:33 /datastore \
         && a2enmod rewrite \
         && mv -f /000-default.conf /etc/apache2/sites-available/ \
         && mv -f /my.cnf /etc/mysql/conf.d/ \
         && rsync -az /etc/apache2/ /datastoresetup/etc-apache2/ \
         && rsync -az /etc/mysql/ /datastoresetup/etc-mysql/ \
         && rsync -az /usr/bin/rathena/ /datastoresetup/usr-bin-rathena/ \
         && rsync -az /var/lib/mysql/ /datastoresetup/var-lib-mysql/ \
         && rsync -az /var/www/html/fluxcp/ /datastoresetup/var-www-html/
        ENV DEBIAN_FRONTEND interactive
    WORKDIR /
     EXPOSE 80 443 3306 5121 6121 6900
     VOLUME /datastore/
     VOLUME /etc/apache2/
     VOLUME /atc/mysql/
     VOLUME /usr/bin/rathena/
     VOLUME /var/lib/mysql/
     VOLUME /var/www/html/
        ENV PHP_UPLOAD_MAX_FILESIZE 10M
        ENV PHP_POST_MAX_SIZE 10M
        CMD bash
 ENTRYPOINT /boottime.sh
