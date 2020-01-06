FROM gregnuj/cyclops-base:alpine3.8
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"
USER root

# Install packages 
RUN set -ex \
    && apk add --no-cache \
    php7 \
    php7-apcu \
    php7-apache2 \
    php7-common \
    php7-curl \
    php7-intl \
    php7-json \
    php7-ldap \
    php7-memcached \
    php7-mcrypt \
    php7-mbstring \
    php7-mysqli \
    php7-odbc \
    php7-pear \
    php7-phar \
    php7-redis \
    php7-simplexml \
    php7-snmp \
    php7-soap \
    php7-sockets \
    php7-ssh2 \
    php7-tokenizer \
    php7-xdebug \
    php7-xml \
    php7-xmlwriter \
    php7-xsl \
    php7-zip \
    php7-pdo \
    php7-pdo_odbc \
    php7-pdo_sqlite \
    php7-pdo_dblib \
    php7-pdo_mysql \
    php7-pdo_pgsql \
    apache2

# get composer from library/composer (uses alpine:3.7)
COPY --from=library/composer /usr/bin/composer /usr/bin/composer
  
# add files in rootfs
ADD ./rootfs /

# add www-data user
RUN set -ex \
    && adduser -u 82 -D -S -G www-data www-data \
    && chown -R www-data:www-data /var/www \
    && mkdir -p /run/apache2 

EXPOSE 22 80 443 9001
