FROM php:7.2-fpm-stretch

# install the PHP extensions we need
RUN set -ex; \
    \
    apt-get update; \
    apt-get install -y \
        git \
        python-pip \
        python-jinja2 \
        openssh-client \
        libjpeg-dev \
        libpng-dev \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        ssmtp \
        git \
        zip \
        libxml2-dev \
        zlib1g-dev \
        zip \
        unzip \
        libpng-dev \
        libmemcached-dev \
        default-libmysqlclient-dev \
        libicu-dev \
        libpq-dev \
        curl \
        libmagickwand-dev \
        iputils-ping \
        telnet \
    ; \
    rm -rf /var/lib/apt/lists/*; \
    \
    docker-php-ext-configure gd --with-png-dir=/usr/include/ --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/; \
    docker-php-ext-install gd soap bcmath mysqli opcache pdo_mysql pdo_pgsql json zip;

#Install Memcached
RUN { \
    curl -L -o /tmp/memcached.tar.gz "https://github.com/php-memcached-dev/php-memcached/archive/php7.tar.gz"; \
    mkdir -p /usr/src/php/ext/memcached; \
    tar -C /usr/src/php/ext/memcached -zxvf /tmp/memcached.tar.gz --strip 1; \
    docker-php-ext-configure memcached; \
    rm /tmp/memcached.tar.gz; \
    docker-php-ext-install memcached; \
}

#Redis
RUN { \
    mkdir -p /usr/src/php/ext/redis; \
    curl -L https://github.com/phpredis/phpredis/archive/3.0.0.tar.gz | tar xvz -C /usr/src/php/ext/redis --strip 1; \
    echo 'redis' >> /usr/src/php-available-exts; \
    docker-php-ext-install redis; \
}

#Imagick
RUN { \
    pecl install imagick; \
    docker-php-ext-enable imagick; \
}

#Install Composer
RUN { \
    php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"; \
    php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer; \
    mkdir -p /cache/composer; \
    }

