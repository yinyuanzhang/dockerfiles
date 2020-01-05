FROM php:7.2-apache

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    zlib1g-dev libpng-dev libjpeg-dev

# Install pdo_mysql extension
RUN docker-php-ext-install pdo_mysql zip gd

# Enable apache mod_rewrite
RUN a2enmod rewrite

# Change document root
ENV APACHE_DOCUMENT_ROOT /var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# Image metadata
ARG VCS_REF
LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/aune-io/docker-base-laravel/"
