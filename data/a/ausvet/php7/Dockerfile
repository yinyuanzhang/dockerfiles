FROM php:7-apache-stretch

LABEL maintainer="ausvet <support@ausvet.com.au>"

EXPOSE 80
EXPOSE 443

# install aditional packages
# try really really hard to update apt
RUN apt-get update || echo $(rm -f /var/lib/apt/lists/* && apt-get update)
RUN apt-get upgrade -y

#    apt-get install -y --no-install-recommends apt-utils && \
RUN apt-get install -y --no-install-recommends \
    git \
    zip \
    unzip \
    libpng-dev

# todo: why is this being installed?
RUN apt-get install -y nfs-common

#    apt-get install -y --no-install-recommends libphp-pclzip && \

RUN apt-get install -y --no-install-recommends \
    zlib1g-dev \
    libmcrypt-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libzip-dev

RUN apt-get install -y --no-install-recommends \
    postgresql-server-dev-all

RUN apt-get install -y --install-recommends nodejs
RUN apt-get install -y \
    node-npm-run-path \
    node-global-modules \
    node-global-prefix
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN pecl install mcrypt-1.0.2 && \
    docker-php-ext-enable mcrypt

RUN docker-php-ext-install zip pdo pdo_pgsql && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) gd

COPY ./php_conf.d/* /usr/local/etc/php/conf.d/

# install assets and configure
RUN a2enmod rewrite
RUN curl --silent --show-error https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer global require fxp/composer-asset-plugin
