FROM debian:stretch-slim

LABEL maintainer="coord.redes@campinas.sp.leg.br"
LABEL version="2.5"
LABEL description="OCS (Open Computers and Software Inventory Next Generation)"

ARG APT_FLAGS="-y --no-install-recommends"

VOLUME /var/lib/mysql

RUN apt-get update ; \
    apt-get ${APT_FLAGS} install \
    apache2 \
    mariadb-client \
    libxml-simple-perl \
    libperl5.24 \
    libdbi-perl \
    libdbd-mysql-perl \
    libapache-dbi-perl \
    libnet-ip-perl \
    libsoap-lite-perl \
    libarchive-zip-perl \
    make \
    build-essential \
    php-pclzip \
    make \
    build-essential \
    libdbd-mysql-perl \
    libnet-ip-perl \
    libxml-simple-perl \
    php-gd \
    php \
    php-mbstring \
    php-soap \
    php-mysql \ 
    php-curl \ 
    php-xml \ 
    php-zip \
    wget \
    tar \
    make ;\
    cpan -i XML::Entities ;\
    /usr/sbin/a2dissite 000-default ;\
    /usr/sbin/a2enmod rewrite ;\
    /usr/sbin/a2enmod ssl ;\
    /usr/sbin/a2enmod authz_user ;\
    wget https://raw.githubusercontent.com/OCSInventory-NG/OCSInventory-Server/master/binutils/docker-download.sh ;\
    sh docker-download.sh 2.5

WORKDIR /tmp/ocs/Apache
RUN perl Makefile.PL ;\
    make ;\
    make install ;\
    cp /usr/share/zoneinfo/Europe/Paris /etc/localtime ;\
    cp -R blib/lib/Apache /usr/local/share/perl/5.20.2/ ;\
    cp -R Ocsinventory /usr/local/share/perl/5.20.2/ ;\
    cp /tmp/ocs/etc/logrotate.d/ocsinventory-server /etc/logrotate.d/ ;\
    mkdir -p /etc/ocsinventory-server/plugins ;\
    mkdir -p /etc/ocsinventory-server/perl ;\
    mkdir -p /usr/share/ocsinventory-reports/ocsreports

ENV APACHE_RUN_USER     www-data
ENV APACHE_RUN_GROUP    www-data
ENV APACHE_LOG_DIR      /var/log/apache2
ENV APACHE_PID_FILE     /var/run/apache2.pid
ENV APACHE_RUN_DIR      /var/run/apache2f
ENV APACHE_LOCK_DIR     /var/lock/apache2
ENV APACHE_LOG_DIR      /var/log/apache2


WORKDIR /tmp/ocs

COPY dbconfig.inc.php /usr/share/ocsinventory-reports/ocsreports/dbconfig.inc.php

RUN cp -R ocsreports/* /usr/share/ocsinventory-reports/ocsreports ;\
    bash -c 'mkdir -p /var/lib/ocsinventory-reports/{download,ipd,logs,scripts,snmp}' ;\
    chmod -R +w /var/lib/ocsinventory-reports ;\
    chown www-data: -R /var/lib/ocsinventory-reports ;\
    cp binutils/ipdiscover-util.pl /usr/share/ocsinventory-reports/ocsreports/ipdiscover-util.pl ;\
    chown www-data: /usr/share/ocsinventory-reports/ocsreports/ipdiscover-util.pl ;\
    chmod 755 /usr/share/ocsinventory-reports/ocsreports/ipdiscover-util.pl ;\
    chmod +w /usr/share/ocsinventory-reports/ocsreports/dbconfig.inc.php ;\
    mkdir -p /var/log/ocsinventory-server/ ;\
    chmod +w /var/log/ocsinventory-server ;\
    chown -R www-data: /usr/share/ocsinventory-reports/ ;\
    echo "<?php" > /tmp/ocs/ocsreports/dbconfig.inc.php ;\
    echo "define('DB_NAME','$OCS_DBNAME')" >> /tmp/ocs/ocsreports/dbconfig.inc.php ;\
    echo "define('SERVER_READ','$OCS_DBSERVER_READ')"  >> /tmp/ocs/ocsreports/dbconfig.inc.php ;\
    echo "define('SERVER_WRITE','$OCS_DBSERVER_WRITE')" >> /tmp/ocs/ocsreports/dbconfig.inc.php ;\
    echo "define('COMPTE_BASE','$OCS_DBUSER')"  >> /tmp/ocs/ocsreports/dbconfig.inc.php ;\
    echo "define('PSWD_BASE','$OCS_DBPASS')" >> /tmp/ocs/ocsreports/dbconfig.inc.php ;\
    echo "?>" >> /tmp/ocs/ocsreports/dbconfig.inc.php

COPY dbconfig.inc.php /usr/share/ocsinventory-reports/ocsreports/dbconfig.inc.php

COPY /conf/ocsinventory-reports.conf /conf/z-ocsinventory-server.conf /etc/apache2/conf-available/
COPY ./scripts/run.sh /root/run.sh

RUN chmod +x /root/run.sh ;\
    ln -s /etc/apache2/conf-available/ocsinventory-reports.conf /etc/apache2/conf-enabled/ocsinventory-reports.conf ;\
    ln -s /etc/apache2/conf-available/z-ocsinventory-server.conf /etc/apache2/conf-enabled/z-ocsinventory-server.conf ;\
    rm /usr/share/ocsinventory-reports/ocsreports/install.php ;\
    apt-get clean ;\
    apt-get autoclean ;\
    apt-get autoremove ;\
    rm -rf /var/lib/apt/lists/* ;\
    rm -rf /var/cache/apt/archives/* ;

EXPOSE 80
EXPOSE 443

CMD ["/bin/bash", "/root/run.sh"]
