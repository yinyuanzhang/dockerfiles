FROM php:7.1-fpm

RUN curl -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/4.2.0.tar.gz && \
    tar xfz /tmp/redis.tar.gz && \
    rm -r /tmp/redis.tar.gz && \
    mkdir -p /usr/src/php/ext && \
    mv phpredis-4.2.0 /usr/src/php/ext/redis && \
    docker-php-ext-install redis

RUN curl -L -o /tmp/mongodb.tar.gz http://pecl.php.net/get/mongodb-1.5.3.tgz && \
    tar xfz /tmp/mongodb.tar.gz && \
    rm -r /tmp/mongodb.tar.gz && \
    mkdir -p /usr/src/php/ext && \
    mv mongodb-1.5.3 /usr/src/php/ext/mongodb && \
    docker-php-ext-install mongodb

RUN curl -L -o /tmp/yaconf.tar.gz https://github.com/laruence/yaconf/archive/yaconf-1.0.7.tar.gz && \
    tar xfz /tmp/yaconf.tar.gz && \
    rm -r /tmp/yaconf.tar.gz && \
    mkdir -p /usr/src/php/ext && \
    mv yaconf-yaconf-1.0.7 /usr/src/php/ext/yaconf && \
    docker-php-ext-install yaconf && \
    mkdir -p /usr/local/etc/php/conf.d/yaconf_directory && \
    echo "yaconf.directory=/usr/local/etc/php/conf.d/yaconf_directory" >> /usr/local/etc/php/conf.d/docker-php-ext-yaconf.ini

RUN docker-php-ext-install exif pdo_mysql pcntl

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer && \
    composer self-update

RUN apt-get update && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev  && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) gd

RUN apt-get install -y libzip-dev zip && \
    docker-php-ext-configure zip --with-libzip && \
    docker-php-ext-install zip

RUN apt-get install -y libxml2-dev && docker-php-ext-install soap;

RUN docker-php-ext-install fileinfo bcmath sockets sysvsem xmlrpc
