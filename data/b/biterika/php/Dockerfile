FROM debian:buster-slim

RUN apt -y update && \
    apt -y install apache2\
		    apache2-utils\
		    # apache modules
		    libapache2-mod-php7.3\
		    libapache2-mod-authnz-pam\
		    libapache2-mod-auth-plain\
		    libapache2-mod-geoip\
		    libapache2-mod-perl2\
		    libapache2-mod-python\
		    libapache2-mod-webauth\
		    libapache2-mod-log-slow\
		    libapache2-mod-fcgid\
		    # php and php modules
		    php7.3\
		    php7.3-bcmath\
		    php7.3-bz2\
		    php7.3-calendar\
		    php7.3-cgi\
		    php7.3-ctype\
		    php7.3-curl\
		    php7.3-dba\
		    php7.3-dom\
		    php7.3-exif\
		    php7.3-fileinfo\
		    php7.3-ftp\
		    php7.3-gd\
		    php7.3-gettext\
		    php7.3-gmp\
		    php7.3-iconv\
		    php7.3-imagick\
		    php7.3-imap\
		    php7.3-intl\
		    php7.3-json\
		    php7.3-ldap\
		    php7.3-mbstring\
		    php7.3-memcache\
		    php7.3-memcached\
		    php7.3-mysqli\
		    php7.3-mysqlnd\
		    php7.3-odbc\
		    php7.3-opcache\
		    php7.3-pdo\
		    php7.3-pgsql\
		    php7.3-phar\
		    php7.3-posix\
		    php7.3-pspell\
		    php7.3-readline\
		    php7.3-recode\
		    php7.3-shmop\
		    php7.3-simplexml\
		    php7.3-snmp\
		    php7.3-soap\
		    php7.3-sockets\
		    php7.3-sqlite3\
		    php7.3-sysvmsg\
		    php7.3-sysvsem\
		    php7.3-sysvshm\
		    php7.3-tidy\
		    php7.3-tokenizer\
		    php7.3-wddx\
		    php7.3-xml\
		    php7.3-xmlreader\
		    php7.3-xmlrpc\
		    php7.3-xmlwriter\
		    php7.3-xsl\
		    php7.3-zip\
		    # install utils
		    curl\
		    wget\
		    tar

RUN curl -sS https://getcomposer.org/installer | php &&\
    mv composer.phar /usr/local/bin/composer

RUN cd /tmp && wget https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz &&\
    tar -zxvf /tmp/ioncube_loaders_lin_x86-64.tar.gz ioncube/ioncube_loader_lin_7.3.so ioncube/ioncube_loader_lin_7.3_ts.so &&\
    mkdir -p /usr/local/ioncube &&\
    cp /tmp/ioncube/ioncube_loader_lin_* /usr/local/ioncube &&\
    rm /tmp/ioncube_loaders_lin_x86-64.tar.gz &&\
    rm -rf /tmp/ioncube

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

EXPOSE 80 443

ENTRYPOINT ["/docker-entrypoint.sh"]
