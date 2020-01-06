FROM ubuntu:16.04

# Labels
LABEL maintainer "oscar.fanelli@gmail.com"

# Environment variables
ENV PROJECT_PATH=/var/www \
    PROJECT_PUBLIC_DIR=public \
    DEBIAN_FRONTEND=noninteractive \
    APACHE_RUN_USER=www-data \
    APACHE_RUN_GROUP=www-data \
    APACHE_LOG_DIR=/var/log/apache2 \
    APACHE_LOCK_DIR=/var/lock/apache2 \
    PHP_INI=/etc/php/5.6/apache2/php.ini \
    TERM=xterm

# Update, upgrade and cURL installation
RUN apt update -q && apt upgrade -yqq && apt install -yqq software-properties-common curl locales

# Locale generator
RUN locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

# Mandatory in order to use PHP v7.1 instead of default one v7.0
RUN add-apt-repository ppa:ondrej/php

# Yarn package managerc
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Utilities, Apache, PHP, and supplementary programs
RUN apt update -q && apt install -yqq --force-yes \
    git \
    npm \
    wget \
    yarn \
    zip \
    apache2 \
    libapache2-mod-php5.6 \
    php5.6 \
    php5.6-bcmath \
    php5.6-curl \
    php5.6-dom \
    php5.6-mbstring \
    php5.6-intl

# NodeJS alias
RUN ln -s "$(which nodejs)" /usr/bin/node

# Apache mods
RUN a2enmod rewrite expires headers

# Apache2 conf
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf
RUN a2enconf fqdn

# php.ini configs
RUN sed -i "s/short_open_tag = .*/short_open_tag = On/" $PHP_INI && \
    sed -i "s/memory_limit = .*/memory_limit = 256M/" $PHP_INI && \
    sed -i "s/display_errors = .*/display_errors = Off/" $PHP_INI && \
    sed -i "s/display_startup_errors = .*/display_startup_errors = Off/" $PHP_INI && \
    sed -i "s/post_max_size = .*/post_max_size = 64M/" $PHP_INI && \
    sed -i "s/upload_max_filesize = .*/upload_max_filesize = 32M/" $PHP_INI && \
    sed -i "s/max_file_uploads = .*/max_file_uploads = 10/" $PHP_INI && \
    sed -i "s/error_reporting = .*/error_reporting = E_ALL \& ~E_DEPRECATED \& ~E_STRICT/" $PHP_INI

# Cleanup
RUN apt purge -yq \
      patch \
      software-properties-common \
      wget && \
    apt autoremove -yqq

# VirtualHost
COPY config/apache-virtualhost.conf /etc/apache2/sites-available/000-default.conf

# Port to expose
EXPOSE 80 443

# Workdir
WORKDIR $PROJECT_PATH

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Start apache
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]