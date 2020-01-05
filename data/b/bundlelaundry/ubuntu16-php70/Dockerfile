FROM ubuntu:xenial

MAINTAINER FAN DENG <fan@bundlelaundry.com>

# Set correct environment variables.
ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

# Our user in the container
USER root
WORKDIR /root

RUN apt-get update && \
    apt-get install -y \
    php7.0 \
    php7.0-cli \
    php7.0-curl \
    php7.0-gd \
    php7.0-mysql \
    php7.0-xsl \
    php7.0-sqlite3 \
    php7.0-dev \
    php7.0-json \
    php7.0-zip \
    php7.0-mbstring \
    php-xdebug \
    php-xml \
    curl \
    git \
    mysql-client \
    build-essential \
    php-pear \
    apache2 \
    libapache2-mod-php7.0 \
    libgtk2.0-0 \
    supervisor \
    fonts-thai-tlwg

# install composer
RUN curl -sS https://getcomposer.org/installer | php \
&& mv composer.phar /usr/local/bin/composer

RUN a2enmod rewrite

# Update the PHP.ini file, upload size to 8M.
RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 8M/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/post_max_size = 8M/post_max_size = 32M/" /etc/php/7.0/apache2/php.ini
RUN sed -i "s/max_execution_time = 30/max_execution_time = 300/" /etc/php/7.0/apache2/php.ini

ENV APACHE_RUN_USER   www-data
ENV APACHE_RUN_GROUP  www-data
ENV APACHE_LOG_DIR    /var/log/apache2
ENV APACHE_LOCK_DIR   /var/lock/apache2
ENV APACHE_PID_FILE   /var/run/apache2.pid

COPY apache2-foreground /usr/local/bin/
COPY apache2-docker /etc/apache2/conf.d/
COPY xdebug_profiler.ini /etc/php/7.0/mods-available/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

WORKDIR /root/

COPY etc/conn-site.conf /etc/apache2/sites-available/
COPY etc/conn-site-ssl.conf /etc/apache2/sites-available/
RUN rm -f /etc/apache2/sites-enabled/000-default*
RUN ln -sf ../sites-available/conn-site.conf /etc/apache2/sites-enabled/conn-site.conf
RUN ln -sf ../sites-available/conn-site-ssl.conf /etc/apache2/sites-enabled/conn-site-ssl.conf

# ENV TZ=Australia/Sydney
# RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["/usr/bin/supervisord"]