FROM php:7.2-fpm

# Fix debconf warnings upon build
ARG DEBIAN_FRONTEND=noninteractive

# Install selected extensions and other stuff
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash - \
   && apt-get update \
   && apt-get install -y build-essential libpng-dev libicu-dev bash-completion nano git git-ftp unzip nodejs \
   && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
   && docker-php-ext-install pdo_mysql sockets \
   && docker-php-ext-enable pdo_mysql sockets \
   && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
