# Docker Adyax
#
#

FROM debian:stable

MAINTAINER Benoît GRUNENBERGER <bgrunenberger@adyax.com>

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update -y && \
	apt-get install -y \
        php5-fpm \
        php5-gd \
        php5-ldap \
        php5-sqlite \
        php5-pgsql \
        php-pear \
        php5-mysql \
        php5-mcrypt \
        #php5-xcache \
        php5-xmlrpc \
        php-apc \
        php5-common \
        php5-curl \
        php5-imagick \
        php5-imap \
        php5-intl \
        php5-json \
        php5-memcache \
        php5-ming \
		php5-ps \
		php5-pspell \
		php5-recode \
		php5-snmp \
		php5-sqlite \
		php5-tidy \
		php5-xmlrpc \
		php5-xsl \
		php5-xdebug && \
	pecl install
		apc \
		bcompiler \
		geoip \
		gmagick \
		lzf \
		mailparse \
		mongo \
		pdflib \
		rar \
		uploadprogress \
		Xdebug && \
    sed 's/;daemonize = yes/daemonize = no/' -i /etc/php5/fpm/php-fpm.conf && \
    apt-get -yq autoclean && \
    apt-get -yq autoremove

ADD php.ini /etc/php5/fpm/php.ini

#VOLUME /etc/php5

EXPOSE 9000

ENTRYPOINT ["php5-fpm"]

#CMD ["service php5-fpm start"]
