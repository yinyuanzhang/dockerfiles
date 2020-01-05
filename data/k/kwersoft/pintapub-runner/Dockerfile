FROM php:7.2
MAINTAINER Max Zamaliev <zamal@inbox.ru>

RUN set -eux ;                 \
    apt-get update -yqq &&     \
    apt-get install gnupg -yqq
RUN set -eux ; \
    curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN set -eux ;                               \
    apt-get install -yqq git                 \
                         nodejs              \
                         postgresql          \
                         postgresql-client   \
                         libcurl4-gnutls-dev \
                         libicu-dev          \
                         libmcrypt-dev       \
                         libvpx-dev          \
                         libjpeg-dev         \
                         libpng-dev          \
                         libxpm-dev          \
                         zlib1g-dev          \
                         libfreetype6-dev    \
                         libxml2-dev         \
                         libexpat1-dev       \
                         libbz2-dev          \
                         libgmp3-dev         \
                         libldap2-dev        \
                         unixodbc-dev        \
                         libpq-dev           \
                         libsqlite3-dev      \
                         libaspell-dev       \
                         libsnmp-dev         \
                         libpcre3-dev        \
                         libtidy-dev         \
                         libzip-dev          \
                         ssh                 \
                         openssh-client      \
                         rsync
RUN set -eux ; \
    docker-php-ext-install curl json intl gd xml bz2 opcache pdo pdo_pgsql
RUN set -eux ;                                          \
    curl -sS https://getcomposer.org/installer | php
