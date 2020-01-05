FROM php:7.3-apache

# https://github.com/docker-library/docs/tree/master/php#how-to-install-more-php-extensions
RUN rm /etc/apt/preferences.d/no-debian-php

# Update all dependencies
RUN apt-get update && apt-get install -y \
		libfreetype6-dev \
				libjpeg62-turbo-dev \
						libpng-dev \
							&& docker-php-ext-configure gd \
								&& docker-php-ext-install -j$(nproc) gd

RUN apt-get install -y libxml2-dev libzip-dev unzip zip
RUN apt-get install -y zlib1g-dev && rm -rf /var/lib/apt/lists/* && docker-php-ext-install zip

# Enable additional Apache modules
RUN a2enmod headers
RUN a2enmod rewrite
RUN a2enmod ssl

# Install MySql connector
RUN docker-php-ext-install pdo pdo_mysql mysqli soap

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs

# Install angular-cli
RUN npm install -g @angular/cli

# Install find-process module
RUN npm install find-process -g

# Create initial dropinbase folder
RUN mkdir /dropinbase
RUN mkdir /dropinbase/runtime
RUN mkdir /dropinbase/runtime/logs
RUN chown www-data:www-data /dropinbase -R
RUN chmod 777 /dropinbase/runtime -R

# TODO /vendor/dropinbase/dropinbase should be copied from somewhere else
# COPY test-app.php /dropinbase/index.php
COPY . /vendor/dropinbase/dropinbase/

WORKDIR /vendor/dropinbase/dropinbase/dropins/setNgxMaterial/angular
RUN npm i
RUN npm run rebuild:shared
RUN npm run build -- --prod
RUN chown www-data:www-data /vendor/dropinbase/dropinbase/dropins/setNgxMaterial/angular/projects/plugins/src -R
RUN chown www-data:www-data /vendor/dropinbase/dropinbase/dropins/setNgxMaterial/angular/src/assets/ -R
RUN chown www-data:www-data /vendor/dropinbase/dropinbase/dropins/setNgxMaterial/dibAdmin/cache/ -R
