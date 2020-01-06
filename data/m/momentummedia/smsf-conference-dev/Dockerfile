FROM php:7.0-apache

# Based on the official Wordpress docker file

RUN a2enmod rewrite expires

RUN chown -R www-data:www-data /var/www/html

RUN mkdir -p /httpdocs

WORKDIR /var/www/html

COPY . /var/www/html

CMD ["apache2-foreground"]

# install the PHP extensions we need
RUN  set -ex; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	\
	apt-get update; \
	apt-get install -y --no-install-recommends \
		libbz2-dev \
		libjpeg-dev \
		libldap2-dev \
		libmcrypt-dev \
		libmemcached-dev \
		libpng-dev \
		libpq-dev \
	; \
	\
	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
	debMultiarch="$(dpkg-architecture --query DEB_BUILD_MULTIARCH)"; \
	docker-php-ext-configure ldap --with-libdir="lib/$debMultiarch"; \
	docker-php-ext-install \
		bz2 \
		gd \
		ldap \
		mcrypt \
		mysqli \
		pdo_mysql \
		pdo_pgsql \
		pgsql \
		zip \
	; \
	\




