FROM phpdockerio/php72-fpm:latest
MAINTAINER eu@brunolima.me
WORKDIR "/application"

# Fix debconf warnings upon build
ARG DEBIAN_FRONTEND=noninteractive

# Install selected extensions and other stuff
RUN apt-get update \
    && apt-get -y --no-install-recommends install  php7.2-mysql php7.2-pgsql php-redis php7.2-sqlite3 php-xdebug php7.2-dba php7.2-enchant php7.2-gd php-gearman php7.2-gmp php-igbinary php-imagick php7.2-imap php7.2-interbase php7.2-intl php7.2-ldap php-mongodb php-msgpack php7.2-odbc php7.2-phpdbg php7.2-pspell php7.2-snmp php7.2-soap php-ssh2 php7.2-sybase php7.2-xmlrpc php7.2-xsl php-yaml \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

# Install git
RUN apt-get update \
    && apt-get -y install git \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
