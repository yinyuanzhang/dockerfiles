FROM ubuntu:18.04

MAINTAINER quyenluu

ENV DEBIAN_FRONTEND=noninteractive

#update ubuntu && install necessary tools
RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
            nano \
            git \
            curl \
            unzip \
            zip \
            apache2 \
            cron && \
    touch /var/log/cron.log

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r mysql && useradd -r -g mysql mysql

RUN apt-get update && apt-get install -y --no-install-recommends gnupg dirmngr && rm -rf /var/lib/apt/lists/*

# add gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& gpgconf --kill all \
	&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y --auto-remove ca-certificates wget

RUN mkdir /docker-entrypoint-initdb.d

RUN apt-get update && apt-get install -y --no-install-recommends \
# for MYSQL_RANDOM_ROOT_PASSWORD
		pwgen \
# for mysql_ssl_rsa_setup
		openssl \
# FATAL ERROR: please install the following Perl modules before executing /usr/local/mysql/scripts/mysql_install_db:
# File::Basename
# File::Copy
# Sys::Hostname
# Data::Dumper
		perl \
	&& rm -rf /var/lib/apt/lists/*

RUN set -ex; \
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
	key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	gpg --batch --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \
	gpgconf --kill all; \
	rm -rf "$GNUPGHOME"; \
	apt-key list > /dev/null

ENV MYSQL_MAJOR 5.7
ENV MYSQL_VERSION 5.7.26-1debian9

RUN echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list

# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't have an explicit way to disable the mysql_install_db codepath besides having a database already "configured" (ie, stuff in /var/lib/mysql/mysql)
# also, we set debconf keys to make APT a little quieter
RUN { \
		echo mysql-community-server mysql-community-server/data-dir select ''; \
		echo mysql-community-server mysql-community-server/root-pass password ''; \
		echo mysql-community-server mysql-community-server/re-root-pass password ''; \
		echo mysql-community-server mysql-community-server/remove-test-db select false; \
	} | debconf-set-selections \
	&& apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}" && rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \
	&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \
# ensure that /var/run/mysqld (used for socket and lock files) is writable regardless of the UID our mysqld instance ends up having at runtime
	&& chmod 777 /var/run/mysqld \
# comment out a few problematic configuration values
	&& find /etc/mysql/ -name '*.cnf' -print0 \
		| xargs -0 grep -lZE '^(bind-address|log)' \
		| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/' \
# don't reverse lookup hostnames, they are usually another container
	&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' > /etc/mysql/conf.d/docker.cnf

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

#install php
ENV PHP_VER 7.3
RUN apt-get update

RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y \
        php${PHP_VER} \
        php${PHP_VER}-cli \
        php${PHP_VER}-curl \
        php${PHP_VER}-fpm \
        php${PHP_VER}-intl \
        php${PHP_VER}-json \
        php${PHP_VER}-mbstring \
        php${PHP_VER}-mysql \
        php${PHP_VER}-xml \
        php${PHP_VER}-zip \
        php${PHP_VER}-ldap \
        php${PHP_VER}-gd \
        php${PHP_VER}-geoip \
        php${PHP_VER}-gnupg \
        php${PHP_VER}-igbinary \
        php${PHP_VER}-imagick \
        php${PHP_VER}-mailparse \
        php${PHP_VER}-memcached \
        php${PHP_VER}-mongodb \
        php${PHP_VER}-oauth \
        php${PHP_VER}-radius \
        php${PHP_VER}-raphf \
        php${PHP_VER}-redis \
        php${PHP_VER}-soap \
        php${PHP_VER}-solr

#install node npm
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY docker-php-entrypoint.sh /usr/local/bin/docker-php-entrypoint.sh
RUN chmod 755 /usr/local/bin/docker-php-entrypoint.sh
#ENTRYPOINT ["/usr/local/bin/docker-php-entrypoint"] 

##<autogenerated>##
COPY apache2-foreground /usr/local/bin/
RUN chmod 755 /usr/local/bin/apache2-foreground
WORKDIR /var/www/html

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

COPY auto-start.sh /auto-start.sh
RUN chmod a+x /auto-start.sh

EXPOSE 80 3306

CMD [ "/auto-start.sh" ]