FROM php:7.2.22-apache

RUN apt-get update

RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y graphviz libfreetype6-dev
RUN apt-get install -y libc-client-dev
RUN apt-get install -y libicu-dev
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y libjpeg62-turbo-dev
RUN apt-get install -y libkrb5-dev
RUN apt-get install -y libmcrypt-dev
RUN apt-get install -y libpng-dev
RUN apt-get install -y libtidy-dev
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libxpm-dev
RUN apt-get install -y libxslt-dev
RUN apt-get install -y python
RUN apt-get install -y ca-certificates
RUN apt-get install -y msmtp
RUN apt-get install -y libpspell-dev
RUN apt-get install -y unzip
RUN apt-get install -y wget
RUN apt-get install -y zlib1g-dev

RUN pecl install timezonedb
RUN pecl install xdebug-2.6.0

RUN docker-php-ext-install -j$(nproc) bcmath
RUN docker-php-ext-install -j$(nproc) calendar
RUN docker-php-ext-install -j$(nproc) exif
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-xpm-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install -j$(nproc) gettext
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl
RUN docker-php-ext-install -j$(nproc) imap
RUN docker-php-ext-install -j$(nproc) intl
RUN docker-php-ext-install -j$(nproc) mysqli
RUN docker-php-ext-install -j$(nproc) pdo_mysql
RUN docker-php-ext-install -j$(nproc) pspell
RUN docker-php-ext-install -j$(nproc) soap
RUN docker-php-ext-install -j$(nproc) sockets
RUN docker-php-ext-install -j$(nproc) tidy
RUN docker-php-ext-install -j$(nproc) wddx
RUN docker-php-ext-install -j$(nproc) xmlrpc
RUN docker-php-ext-install -j$(nproc) xsl
RUN docker-php-ext-install -j$(nproc) zip

RUN a2enmod rewrite ssl
