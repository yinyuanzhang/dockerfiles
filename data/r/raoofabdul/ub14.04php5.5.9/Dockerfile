FROM ubuntu:14.04
MAINTAINER Abdulraoof Arakkal <raoofabdul@gmail.com>

# disable interactive functions
ENV DEBIAN_FRONTEND noninteractive

# Install apache, PHP, and supplimentary programs.
RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y apache2 \
    php5 libapache2-mod-php5  \
    php5-fpm php5-cli php5-mysql \
    php5-apcu php5-intl php5-imagick php5-mcrypt php5-json php5-gd php5-curl \
    mcrypt


# Enable apache mods.
RUN a2enmod php5
RUN a2enmod rewrite

# Update the PHP.ini file, enable <? ?> tags and quieten logging.
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/apache2/php.ini
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING | E_PARSE/" /etc/php5/apache2/php.ini

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Expose apache.
EXPOSE 80

# Copy this repo into place.
ADD www/html /var/www/site

# Update the default apache site with the config we created.
ADD apache/config/apache-config.conf /etc/apache2/sites-enabled/000-default.conf

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND


# Install dependencies
RUN apt-get -y install iputils-ping

RUN apt-get -y install git

RUN apt-get update && \
    apt-get -y install curl nano && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
