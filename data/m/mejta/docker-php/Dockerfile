FROM php:5.6-apache

# Custom php.ini
COPY php.ini /usr/local/etc/php/

# Set default shell
SHELL ["/bin/bash", "-c"]

# configure Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf; \
    a2enmod rewrite; \
    service apache2 restart

# Install systemlibs, and php extensions
RUN apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get -y install --no-install-recommends \
    autoconf checkinstall libtool make nasm pkg-config \
    libpng12-dev \
    libmcrypt-dev \
    libjpeg-dev \
    libpq-dev \
    libsqlite3-dev \
    zip \
    unzip \
    libc-client-dev libkrb5-dev \
    ; \
	rm -rf /var/lib/apt/lists/*; \
	\
	docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
    docker-php-ext-configure imap --with-kerberos --with-imap-ssl; \
	docker-php-ext-install gd mysqli opcache mcrypt pdo pdo_pgsql pdo_mysql pdo_sqlite zip

RUN a2enmod rewrite expires deflate headers

VOLUME /var/www/html

CMD ["apache2-foreground"]
