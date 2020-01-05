FROM php:7.2.6-apache
MAINTAINER Xavier Casahuga <casahuga@gmail.com>

COPY apache2.conf /bin/

# CREATE APACHE PUBLIC FOLDER
RUN mkdir -p /var/www/html/public/

RUN a2enmod rewrite expires include deflate

# install the PHP extensions we need
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         libpng-dev \
         libjpeg-dev \
         libpq-dev \
         libmcrypt-dev \
         libldap2-dev \
         libldb-dev \
         libicu-dev \
         libgmp-dev \
         libmagickwand-dev \
         cron \
         openssh-server \
                 curl \
                 git \
                 mysql-client \
                 nano \
                 sudo \
                 tcptraceroute \
                 vim \
                 wget \
                 supervisor \
                 rsyslog \
    && echo "root:Docker!" | chpasswd \
    && echo "cd /home" >> /etc/bash.bashrc \
    && ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \
    && ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so \
    && ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \
    && rm -rf /var/lib/apt/lists/* \
    && pecl install imagick-beta \
    && pecl install mcrypt-1.0.1 \
    && pecl install -o -f redis \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd \
         mysqli \
         opcache \
         pdo \
         pdo_mysql \
         pdo_pgsql \
         pgsql \
         ldap \
         intl \
         gmp \
         zip \
         bcmath \
         mbstring \
         pcntl \
    && docker-php-ext-enable imagick \
    && docker-php-ext-enable redis \
    && docker-php-ext-enable mcrypt 

RUN   \
   rm -f /var/log/apache2/* \
   && rmdir /var/lock/apache2 \
   && rmdir /var/run/apache2 \
   && rmdir /var/log/apache2 \
   && chmod 777 /var/log \
   && chmod 777 /var/run \
   && chmod 777 /var/lock \
   && cp /bin/apache2.conf /etc/apache2/apache2.conf \
   && rm -rf /var/www/html \
   && rm -rf /var/log/apache2 \
   && mkdir -p /home/LogFiles \
   && ln -s /home/site/wwwroot /var/www/html \
   && ln -s /home/LogFiles /var/log/apache2 \
   && rm /etc/apache2/sites-available/000-default.conf \
   && rm /etc/apache2/sites-enabled/000-default.conf


RUN { \
                echo 'opcache.memory_consumption=256'; \
                echo 'opcache.interned_strings_buffer=16'; \
                echo 'opcache.max_accelerated_files=7000'; \
                echo 'opcache.revalidate_freq=600'; \
                echo 'opcache.fast_shutdown=1'; \
                echo 'opcache.validate_timestamps=0'; \
                echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN { \
                echo 'error_log=/var/log/apache2/php-error.log'; \
                echo 'display_errors=Off'; \
                echo 'log_errors=On'; \
                echo 'display_startup_errors=Off'; \
                echo 'date.timezone=UTC'; \
    } > /usr/local/etc/php/conf.d/php.ini

COPY sshd_config /etc/ssh/

EXPOSE 2222 80

ENV APACHE_RUN_USER www-data
ENV PHP_VERSION 7.2.6

ENV PORT 80
ENV WEBSITES_PORT 80
ENV WEBSITE_ROLE_INSTANCE_ID localRoleInstance
ENV WEBSITE_INSTANCE_ID localInstance
ENV PATH ${PATH}:/home/site/wwwroot/public

WORKDIR /var/www/html

# Configure data volume
#RUN mkdir -p  /home/site/wwwroot/storage/app/ \
#    && mkdir -p  /var/www/html/storage/app/ \
#    && ln -s /home/site/wwwroot/storage/app  /var/www/html/storage/app \
#    && mkdir -p  /home/site/wwwroot/storage/framework/sessions/ \
#    && mkdir -p  /var/www/html/storage/framework/sessions/ \
#    && ln -s /home/site/wwwroot/storage/framework/sessions  /var/www/html/storage/framework/sessions \
#    && mkdir -p  /home/site/wwwroot/storage/storage/logs/ \
#    && mkdir -p  /var/www/html/storage/storage/logs/ \
#    && ln -s /home/site/wwwroot/storage/storage/logs  /var/www/html/storage/storage/logs

# Configure directory permissions for the web server
RUN mkdir -p /var/www/html/bootstrap/cache/ \
    && mkdir -p /var/www/html/storage/

RUN chgrp -R www-data storage /var/www/html/bootstrap/cache
RUN chmod -R ug+rwx storage /var/www/html/bootstrap/cache

RUN chgrp -R www-data storage /var/www/html/storage
RUN chmod -R ug+rwx storage /var/www/html/storage
