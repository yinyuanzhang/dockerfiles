# REF: https://github.com/pietheinstrengholt/laravel-docker-k8s
FROM php:7.1.3-fpm

# Install packages and php extenstions
RUN apt-get update && apt-get install -y \
        libpq-dev \
        libmcrypt-dev \
        postgresql-client \
        git \
        curl \
        zlib1g-dev \
        libbz2-dev \
    && docker-php-ext-install -j$(nproc) mcrypt \
    && docker-php-ext-install -j$(nproc) pdo \
    && docker-php-ext-install -j$(nproc) pdo_pgsql \
    && docker-php-ext-install -j$(nproc) zip \
    && docker-php-ext-install -j$(nproc) bz2 \
    && docker-php-ext-install  mbstring

# Get vim so we can edit files if needed
RUN apt-get install vim -y

# Supervisor to manage processes
RUN apt-get install supervisor -y

# Install nginx web server
RUN apt-get install -y nginx  && \
    rm -rf /var/lib/apt/lists/*

# Copy the app into the image
COPY . /var/www/html
WORKDIR /var/www/html

# Get composer and install
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer
RUN composer install --prefer-source --no-interaction

RUN rm /etc/nginx/sites-enabled/default

COPY ./deploy/deploy.conf /etc/nginx/conf.d/default.conf

RUN mv /usr/local/etc/php-fpm.d/www.conf /usr/local/etc/php-fpm.d/www.conf.backup
COPY ./deploy/www.conf /usr/local/etc/php-fpm.d/www.conf

RUN usermod -a -G www-data root
RUN chgrp -R www-data storage

RUN chown -R www-data:www-data ./storage
RUN chmod -R 0777 ./storage

RUN ln -s ./secret/.env .env

RUN chmod +x ./deploy/run.sh

ENTRYPOINT ["/bin/sh", "./deploy/run.sh"]

EXPOSE 80
