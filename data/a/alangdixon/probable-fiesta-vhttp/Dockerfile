# FROM drupal:7
# from https://www.drupal.org/requirements/php#drupalversions
ARG VSITE_PHP_VERSION=7.0
FROM php:${VSITE_PHP_VERSION}-apache

RUN a2enmod rewrite

# install the PHP extensions we need
# added libxml2-dev for dom, curl extension
# Added a few more extensions for civicrm and/or contrib modules (varnish)
RUN set -ex \
	&& buildDeps=' \
		libjpeg62-turbo-dev \
		libpng-dev \
		libpq-dev \
                libxml2-dev \ 
                libmagickwand-dev \
                libmcrypt-dev \
                libicu-dev \
                libc-client-dev \
                libkrb5-dev \
	' \
	&& apt-get update && apt-get install -y --no-install-recommends $buildDeps && rm -rf /var/lib/apt/lists/* \
	&& docker-php-ext-configure gd \
		--with-jpeg-dir=/usr \
		--with-png-dir=/usr \
	&& docker-php-ext-configure imap \
		--with-imap-ssl \
		--with-kerberos \
	&& docker-php-ext-install -j "$(nproc)" gd mbstring pdo pdo_mysql pdo_pgsql zip \
opcache \
mysqli \
dom \
soap \
sockets \
mcrypt \
intl \
bcmath \
gettext \
imap \
	&& apt-mark manual \
		libjpeg62-turbo \
		libpq5 
# RUN apt-get update && apt-get install -y mariadb-client sudo vim git 
#  no php-pear for 7.0 or above, so fail silently
RUN pecl install -o redis \
  &&  docker-php-ext-enable redis
# this may not work for 5.6 .., 
RUN pecl install -o imagick \
  && docker-php-ext-enable imagick 
RUN apt-get purge -y --auto-remove $buildDeps
# lets enable mode_expires
RUN a2enmod expires

WORKDIR /var/www/html

# e.g. https://www.drupal.org/node/3060/release
ARG DRUPAL_VERSION=7.59
ARG DRUPAL_MD5=7e09c6b177345a81439fe0aa9a2d15fc
ARG CIVICRM_VERSION=5.5.1

RUN curl -fSL "https://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -o drupal.tar.gz \
	&& echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - \
	&& tar -xz --strip-components=1 -f drupal.tar.gz \
	&& rm drupal.tar.gz \
	&& chown -R www-data:www-data sites
WORKDIR /var/www/html/sites/all/modules
RUN curl -fSL "https://download.civicrm.org/civicrm-${CIVICRM_VERSION}-drupal.tar.gz" -o civicrm.tar.gz \
	&& tar -xz --strip-components=1 -f civicrm.tar.gz \
	&& rm civicrm.tar.gz 
WORKDIR /var/www/html
CMD ["apache2-foreground"]
