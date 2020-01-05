FROM php:7.2-apache
# Based on https://github.com/getgrav/docker-grav
MAINTAINER Bao Ho <hotribao@gmail.com>

# timezone
# The timezone name must be in this list: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# If using Etc/UTC, after moving tzdata, the "date" command will result a GMT! So using UTC instead of Etc/UTC
ENV TZ="UTC"

# for using terminal in container, for text editos, less/tail....
ENV TERM="xterm"

# Enable Apache Rewrite + Expires Module
RUN a2enmod rewrite expires

# Install dependencies
RUN apt-get update && apt-get install -y \
        unzip \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libyaml-dev \
        wget \
    && docker-php-ext-install opcache \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install zip

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
		echo 'opcache.memory_consumption=128'; \
		echo 'opcache.interned_strings_buffer=8'; \
		echo 'opcache.max_accelerated_files=4000'; \
		echo 'opcache.revalidate_freq=2'; \
		echo 'opcache.fast_shutdown=1'; \
		echo 'opcache.enable_cli=1'; \
		echo 'upload_max_filesize=128M'; \
		echo 'post_max_size=128M'; \
		echo 'expose_php = Off'; \
	} > /usr/local/etc/php/conf.d/php-recommended.ini


RUN pecl install apcu \https://github.com/getgrav/docker-grav \
    && pecl install yaml \
    && docker-php-ext-enable apcu yaml

# Set user to www-data
RUN chown www-data:www-data /var/www
USER www-data

# grav (core) or grav-admin (core + admin)
ENV GRAV='grav'
# Define Grav version and expected SHA1 signature
ENV GRAV_VERSION 1.6.17
# ENV GRAV_SHA1 af0433facdae1afeb1d973a66db2315c5022b10d

# Install grav
WORKDIR /var/www
RUN wget -O ${GRAV}.zip -S https://getgrav.org/download/core/${GRAV}/${GRAV_VERSION} && \
    # echo "$GRAV_SHA1 ${GRAV}.zip" | sha1sum -c - && \
    unzip ${GRAV}.zip && \
    mv -T /var/www/${GRAV} /var/www/html && \
    rm ${GRAV}.zip

# ######
# Install grav plugin
WORKDIR /var/www/html
# https://github.com/trilbymedia/grav-plugin-page-toc
RUN bin/gpm install page-toc && \
    bin/gpm install breadcrumbs && \
    bin/gpm install highlight && \
    bin/gpm install sitemap

WORKDIR /var/www

# ######
# customize apache2
# USER root
# enable log_forensic to dump request details
# work together with directive "ForensicLog" in file apache2.conf
# RUN a2enmod log_forensic
USER www-data
COPY apache2/apache2.conf /etc/apache2/apache2.conf
COPY apache2/ports.conf /etc/apache2/ports.conf
COPY apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf

# When being on heroku, heroku will assign each container a random port in this variable
ENV PORT 80

# ######
# custom config
# In development, this is volumn mapping for speedy
COPY user/config /var/www/html/user/config

# ######
# used by http://wakemydyno.com/ to keep free-dyno heroku app wake-up
COPY webroot/wakemydyno.txt /var/www/html/wakemydyno.txt

# ######
# build site content
#
# Remove default content to copy our own
RUN rm -rf /var/www/html/user/pages
# In development, this is volumn mapping for speedy
COPY user/pages /var/www/html/user/pages

# #####
# custom theme
# In development, this is volumn mapping for speedy
COPY user/themes/ciy-quark /var/www/html/user/themes/ciy-quark

# Return to root user
USER root
