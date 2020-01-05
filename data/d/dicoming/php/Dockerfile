# Set the base image
FROM php:5.6-apache

# File Author / Maintainer
MAINTAINER Bukharov Sergey <bukharovSI@gmail.com>

# install php dependencies
RUN apt-get update && apt-get install -y \
        php5-pgsql \
        postgresql-client \
        php5-mongo \
        libxml2-dev \
        php-soap \
        libpq-dev \
        php-pear \
        curl \
        libmemcached-dev \
        libcurl4-openssl-dev \
        git-core \
        nano \
    && docker-php-ext-install pdo \
    && docker-php-ext-install pgsql \
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-install soap

#for nano working
ENV TERM xterm

# preconfiguring apache
RUN a2enmod rewrite && a2enmod headers && a2enmod proxy && a2enmod proxy_http
RUN echo "export DISPLAY=':0'" >> /etc/apache2/envvars
VOLUME /var/log/apache2
EXPOSE 80

# configure envarionments
RUN echo "date.timezone=Europe/Moscow" > $PHP_INI_DIR/conf.d/date_timezone.ini