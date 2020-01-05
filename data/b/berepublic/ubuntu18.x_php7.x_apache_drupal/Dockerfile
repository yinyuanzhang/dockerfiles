FROM ubuntu:18.04

MAINTAINER BeRepublic

ENV DEBIAN_FRONTEND noninteractive
ENV COMPOSER_DISABLE_XDEBUG_WARN 1

# Upgrade the container
RUN apt-get clean && \
    apt-get update && \
    apt-get upgrade -y

# Utils
RUN apt-get install -y nano unzip build-essential software-properties-common apt-utils curl
RUN add-apt-repository -y ppa:ondrej/php
RUN add-apt-repository -y ppa:git-core/ppa
RUN apt-get update

# Apache + PHP
RUN apt-get install -y apache2 libapache2-mod-php7.3 php7.3 php7.3-common php7.3-cli php7.3-fpm
RUN apt-get update && apt-get install -y php7.3-mysql php7.3-intl php7.3-xml php7.3-mbstring php7.3-gd php7.3-curl php-xdebug
RUN apt-get update

# Install tools
RUN apt-get install -y locales

RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.3/fpm/php.ini
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php/7.3/cli/php.ini

# Install git
RUN apt-get install -y git

# MySQL
RUN apt-get install -y mysql-client

# GD extension
RUN apt-get install -y libpng-dev

# PHPUnit
RUN curl -fsSL https://phar.phpunit.de/phpunit-6.5.phar -o phpunit-6.5.phar && \
    mv phpunit-6.5.phar /usr/local/bin/phpunit && \
    chmod +x /usr/local/bin/phpunit && \
    phpunit --version

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

RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.3/fpm/php-fpm.conf
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.3/fpm/php.ini

RUN mkdir /log
RUN mkdir -p     /var/www

# Enable apache mods.
RUN a2enmod php7.3
RUN a2enmod rewrite

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

# Configure PHP
ADD php.ini /etc/php/7.3/apache2/conf.d/

# Configure Virtualhost
ADD default.conf /etc/apache2/sites-enabled/000-default.conf

RUN a2enmod rewrite expires

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose apache.
EXPOSE 80 443

# Set working dir
WORKDIR /var/www

CMD ["apache2ctl", "-D", "FOREGROUND"]

