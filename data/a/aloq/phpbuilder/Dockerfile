FROM php:cli

# Show current php version
RUN php --version \
    && php --modules

# Get repository and install wget and vim
RUN apt-get update && apt-get install --no-install-recommends -y \
        wget \
        vim \
        git \
        unzip \
        openssh-client \
        rsync \
        gnupg2

# Add PostgreSQL repository
#RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" > /etc/apt/sources.list.d/pgdg.list
#RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
#      apt-key add -

# Install PHP extensions deps
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libpq-dev \
        zlib1g-dev \
        libicu-dev \
        libzip-dev \
        g++ \
        unixodbc-dev \
        libxml2-dev \
        libaio-dev \
        libmemcached-dev \
        freetds-dev \
        libssl-dev \
        openssl

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- \
        --install-dir=/usr/local/bin \
        --filename=composer

# Install Sentry CLI
RUN curl -sL https://sentry.io/get-cli/ | bash

# Install PHP extensions
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure pdo_dblib --with-libdir=/lib/x86_64-linux-gnu \
    && pecl install sqlsrv-5.6.1 \
    && pecl install pdo_sqlsrv-5.6.1 \
    && pecl install redis \
    && pecl install memcached \
    && pecl install xdebug \
    && pecl install channel://pecl.php.net/mcrypt-1.0.2 \
    && docker-php-ext-install \
            iconv \
            mbstring \
            intl \
            gd \
            pgsql \
            mysqli

# Install more PHP extensions
RUN docker-php-ext-install \
            pdo_pgsql \
            pdo_mysql \
            #pdo_dblib \
            soap \
            sockets \
            zip \
            pcntl \
            ftp

# Enable extensions
RUN docker-php-ext-enable \
            sqlsrv \
            pdo_sqlsrv \
            redis \
            memcached \
            opcache \
            xdebug


# Install APCu and APC backward compatibility
RUN pecl install apcu \
    && pecl install apcu_bc-1.0.3 \
    && docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini \
    && docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini

# Install PHPUnit
RUN wget https://phar.phpunit.de/phpunit.phar -O /usr/local/bin/phpunit \
    && chmod +x /usr/local/bin/phpunit \
    && phpunit --version

# Clean repository
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir --parents /root/.ssh && chmod 700 /root/.ssh

# RUN pecl install xdebug-2.6.1 \
#    && docker-php-ext-enable xdebug
