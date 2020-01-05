FROM ubuntu:16.04

MAINTAINER Tran Duc Thang <thangtd90@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive
# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common locales

RUN locale-gen en_US.UTF-8

ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=UTF-8
ENV LANG=en_US.UTF-8
ENV TERM xterm

# Add the "PHP 7" ppa
RUN add-apt-repository -y \
    ppa:ondrej/php

# Install PHP-CLI 7, some PHP extentions and some useful Tools with APT
RUN apt-get update && apt-get install -y --force-yes \
        php7.2-cli \
        php7.2-common \
        php7.2-curl \
        php7.2-json \
        php7.2-xml \
        php7.2-mbstring \
        php7.2-mysql \
        php7.2-pgsql \
        php7.2-sqlite \
        php7.2-sqlite3 \
        php7.2-zip \
        php7.2-memcached \
        php7.2-gd \
        php7.2-fpm \
        php7.2-xdebug \
        php7.2-bcmath \
        php7.2-intl \
        php7.2-dev \
        libcurl4-openssl-dev \
        libedit-dev \
        libssl-dev \
        libxml2-dev \
        xz-utils \
        sqlite3 \
        libsqlite3-dev \
        git \
        curl \
        vim \
        nano \
        net-tools \
        pkg-config \
        iputils-ping

# remove load xdebug extension (only load on phpunit command)
# RUN sed -i 's/^/;/g' /etc/php/7.2/cli/conf.d/20-xdebug.ini

# Load xdebug Zend extension with phpunit command
# RUN echo "alias phpunit='php -dzend_extension=xdebug.so /var/www/laravel/vendor/bin/phpunit'" >> ~/.bashrc

# Add bin folder of composer to PATH.
RUN echo "export PATH=${PATH}:/var/www/laravel/vendor/bin:/root/.composer/vendor/bin" >> ~/.bashrc

# Install mongodb extension
RUN pecl channel-update pecl.php.net && pecl install mongodb
RUN echo "extension=mongodb.so" >> /etc/php/7.2/cli/php.ini

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g eslint babel-eslint eslint-plugin-react yarn

# Install SASS
RUN apt-get install -y ruby ruby-dev \
    && gem install sass

# Install Composer, PHPCS and Framgia Coding Standard,
# PHPMetrics, PHPDepend, PHPMessDetector, PHPCopyPasteDetector
RUN curl -s http://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && composer global require 'squizlabs/php_codesniffer' \
        'phpmetrics/phpmetrics' \
        'pdepend/pdepend' \
        'phpmd/phpmd' \
        'sebastian/phpcpd' \
    && cd ~/.composer/vendor/squizlabs/php_codesniffer/src/Standards \
    && git clone https://github.com/wataridori/framgia-php-codesniffer.git Framgia

# Create symlink
RUN ln -s /root/.composer/vendor/bin/phpcs /usr/bin/phpcs \
    && ln -s /root/.composer/vendor/bin/pdepend /usr/bin/pdepend \
    && ln -s /root/.composer/vendor/bin/phpmetrics /usr/bin/phpmetrics \
    && ln -s /root/.composer/vendor/bin/phpmd /usr/bin/phpmd \
    && ln -s /root/.composer/vendor/bin/phpcpd /usr/bin/phpcpd

# Install framgia-ci-tool
RUN curl -o /usr/bin/framgia-ci https://raw.githubusercontent.com/framgiaci/framgia-ci-cli/master/dist/framgia-ci \
    && chmod +x /usr/bin/framgia-ci

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/www/laravel
