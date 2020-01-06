FROM php:7.3-fpm

RUN chmod -R 777 /tmp

ENV COMPOSER_ALLOW_SUPERUSER=1
ENV COMPOSER_NO_INTERACTION=1

# ghostscript is needed for PDF conversion
# libpq-dev is needed for missing includes for pdo_pgsql
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libmcrypt-dev \
    libmagickwand-dev \
    ghostscript \
    libpq-dev \
    libzip-dev \
    redis-tools

RUN pecl install zip \
    && pecl install imagick \
    && pecl install redis \
	&& pecl install mcrypt-1.0.2

RUN docker-php-ext-enable zip \
    && docker-php-ext-enable imagick \
    && docker-php-ext-enable mcrypt \
    && docker-php-ext-install pdo pdo_mysql \
    && docker-php-ext-install gd \
    && docker-php-ext-enable redis \
    && docker-php-ext-install pcntl

RUN  pecl install xdebug-2.7.0beta1 \
    && docker-php-ext-enable xdebug

COPY . /var/www
RUN chown -R www-data:www-data /var/www
RUN chmod -R 777 /var/www/storage
RUN chmod -R +x /var/www/bin

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
