# Base image
FROM ubuntu:14.04

MAINTAINER Erik Kaareng-Sunde esu@enonic.com

#### Inspired by the tianon/apache2 image ####

RUN apt-get update && apt-get install -y apache2

# let's copy a few of the settings from /etc/init.d/apache2
ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars
# and then a few more from $APACHE_CONFDIR/envvars itself
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C

# ...
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

# make CustomLog (access log) go to stdout instead of files
#  and ErrorLog to stderr
RUN find "$APACHE_CONFDIR" -type f -exec sed -ri ' \
    s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
    s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
' '{}' ';'

COPY sites-available/000-default.conf /etc/apache2/sites-available/000-default.conf

# Enabling ssl
COPY sites-available/default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN a2ensite default-ssl
RUN a2enmod ssl

COPY sites-available/statuspage.conf /etc/apache2/sites-available/statuspage.conf
RUN a2ensite statuspage

#VOLUME /etc/apache2 /etc/ssl /var/log/apache2 /var/www/html


EXPOSE 80 443 8001

CMD apache2 -DFOREGROUND
