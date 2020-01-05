FROM php:7.2-fpm

ENV USER 1000
ENV GROUP 100

ENV COMPOSER_ALLOW_SUPERUSER 1

# Update system
RUN apt-get update -y && apt-get upgrade -y

# Install packages
RUN apt-get install -y \
    git \
	libfreetype6-dev \
	libicu-dev \
	libjpeg62-turbo-dev \
	libssh2-1 \
	libssh2-1-dev \
	libssl-dev \
	zlib1g-dev \
	zip unzip

# PDO, zip, FTP, mbstring, intl
RUN docker-php-ext-install -j$(nproc) \
    ftp \
    intl \
    mbstring \
    pdo \
    pdo_mysql \
    zip

# GD extension
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  &&  \
    docker-php-ext-install gd

RUN pecl install ssh2-1.1.2 \
    && docker-php-ext-enable ssh2

RUN docker-php-ext-configure opcache --enable-opcache \
    && docker-php-ext-install opcache

# Install Composer:
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

RUN useradd -u "$USER" -g "$GROUP" -G www-data app && \
  mkdir -p /home/app/.composer && \
  chown app /home/app/.composer

WORKDIR /var/www/vw-crm.aws.projects.clever-age.net
