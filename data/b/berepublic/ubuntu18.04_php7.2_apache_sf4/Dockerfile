FROM ubuntu:18.04

MAINTAINER BeRepublic

ENV DEBIAN_FRONTEND noninteractive
ENV COMPOSER_DISABLE_XDEBUG_WARN 1

# Upgrade the container
RUN apt-get clean && \
    apt-get update && \
    apt-get upgrade -y

# Nginx-PHP Installation
RUN apt-get install -y nano unzip build-essential software-properties-common apt-utils curl
RUN add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository -y ppa:git-core/ppa
RUN apt-get update

# Install php 7.2
RUN apt-get install -y libapache2-mod-php7.2 php7.2 php7.2-common php7.2-cli php7.2-fpm

# Install extension php
RUN apt-get install -y php7.2-mongodb php7.2-curl php7.2-gd php7.2-intl php7.2-json php7.2-xml php7.2-zip php7.2-mbstring php7.2-bcmath

# Install LDAP
RUN apt-get install -y php7.2-ldap

# Install tools
RUN apt-get install -y locales

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.2/cli/php.ini

# Install apache
RUN apt-get install -y apache2

# Install git
RUN apt-get install -y git

# Install xdebug
RUN apt-get install -y php7.2-xdebug

# Cleanup
RUN apt-get remove --purge -y python-software-properties && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Ensure UTF-8
RUN locale-gen en_US.UTF-8 en_GB.UTF-8 es_ES.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.2/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.2/fpm/php.ini

RUN mkdir /log
RUN mkdir -p     /var/www

# Configure PHP
ADD php.ini /etc/php/7.2/apache2/conf.d/

# Configure vhost
ADD default.conf /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod rewrite expires

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add path the phpunit (project level)
ENV PATH /var/www/vendor/bin:$PATH

EXPOSE 80 443

# Set working dir
WORKDIR /var/www

CMD ["apache2ctl", "-D", "FOREGROUND"]
