FROM php:apache

RUN apt-get -y update
ENV LIBVIRT_PHP_VERSION 0.5.4

RUN apt-get -y install libmagickwand-dev --no-install-recommends && \
    pecl install imagick && \
    docker-php-ext-enable imagick

RUN apt-get -y install libvirt-dev libxml2-utils xsltproc wget && \
    wget -O /tmp/libvirt-php-$LIBVIRT_PHP_VERSION.tar.gz http://libvirt.org/sources/php/libvirt-php-$LIBVIRT_PHP_VERSION.tar.gz && \
    cd /tmp && \
    tar xvfz libvirt-php-$LIBVIRT_PHP_VERSION.tar.gz && \
    cd libvirt-php-$LIBVIRT_PHP_VERSION && \
    ./configure && \
    make && \
    make install && \
    docker-php-ext-enable libvirt-php && \
    rm -rf /tmp/pear /tmp/libvirt-php-$LIBVIRT_PHP_VERSION.tar.gz /tmp/libvirt-php-$LIBVIRT_PHP_VERSION
