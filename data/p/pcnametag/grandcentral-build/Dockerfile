#FROM php:7.0-cli
FROM php:7.0-apache

# Magento 2.1.x build and deployment base image 

MAINTAINER Ben Yanke <byanke@pcnametag.com>

# Loosely based on https://github.com/meanbee/docker-magento2

######################
# Install Dependencies
######################

# Install dependencies
RUN apt-get update \
  && apt-get install -y \
    libfreetype6-dev \ 
    libicu-dev \ 
    libjpeg62-turbo-dev \ 
    libmcrypt-dev \ 
    libpng-dev \ 
    libxslt1-dev \ 
    sendmail-bin \ 
    sendmail \ 
    sudo \ 
    cron \ 
    rsyslog \ 
    mysql-client \ 
    wget \
    git

# Enable mod-rewrite
RUN a2enmod rewrite

# Install dumb-init
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 && chmod +x /usr/local/bin/dumb-init

# Configure the gd library
RUN docker-php-ext-configure \
  gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

# Install required PHP extensions

RUN docker-php-ext-install \
  dom \ 
  gd \ 
  intl \ 
  mbstring \ 
  pdo_mysql \ 
  xsl \ 
  zip \ 
  soap \ 
  bcmath \ 
  mcrypt

# Apache logs to STDOUT for docker logs
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
    ln -sf /proc/self/fd/1 /var/log/apache2/error.log

ENV PHP_MEMORY_LIMIT 2G
ENV PHP_ENABLE_XDEBUG false
ENV MAGENTO_ROOT /var/www/magento

ENV DEBUG false
ENV UPDATE_UID_GID false
