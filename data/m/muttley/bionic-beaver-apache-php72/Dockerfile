FROM ubuntu:18.04

RUN useradd webmgr -u 600

RUN apt update && apt -y upgrade && DEBIAN_FRONTEND=noninteractive apt -y install \
	git \
        apache2 \
	php7.2 \
	php7.2-common \
	php7.2-mysql \	
	php7.2-curl \
	php7.2-cli \
	php7.2-json \
	php7.2-sqlite3 \
	php7.2-intl \
	php7.2-dev \
	php7.2-gd \
	php7.2-opcache \
	php7.2-zip \
        php7.2-ldap \
	curl \
	php-xdebug \
	vim

# Enable apache mods.
RUN a2enmod php7.2
RUN a2enmod rewrite

#run pecl install mongodb
#run echo "extension=mongodb.so" >> /etc/php/7.2/apache2/php.ini


# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php/7.2/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php/7.2/apache2/php.ini
RUN sed -i "s/display_errors = Off/display_errors = On/" /etc/php/7.2/apache2/php.ini

#RUN sed -i "s/128M/512M/" /etc/php/7.2/apache2/php.ini
# Manually set up the apache environment variables
ENV APACHE_RUN_USER webmgr
ENV APACHE_RUN_GROUP webmgr
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Expose apache.
EXPOSE 80

VOLUME ["/var/www/html", "/var/log/apache2", "/etc/apache2/sites-enabled", "/etc/apache2/", "/etc/php/7.2/apache2/"]


CMD /usr/sbin/apache2ctl -D FOREGROUND
