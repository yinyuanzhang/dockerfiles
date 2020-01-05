# 暂时使用当前最新版的7.3
FROM php:7.3-cli

# 依赖
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    libpng-dev \
    zlib1g-dev \
    libzip-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libsasl2-dev \
    libmemcached-dev \
    libicu-dev \
    libgmp3-dev \
    libzip4 \
    libpcre3 \
    libpcre3-dev \
    libssl-dev
# openssh 
RUN apt-get install -y openssh-client
# iconv
RUN docker-php-ext-install -j$(nproc) iconv
# zip
RUN docker-php-ext-install zip && docker-php-ext-enable zip
# redis
RUN pecl install redis && docker-php-ext-enable redis
# gd
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd
# swoole
RUN pecl install swoole-4.3.1 && docker-php-ext-enable swoole
# bcmath  
RUN docker-php-ext-install bcmath
# sockets
RUN docker-php-ext-install sockets
RUN docker-php-ext-install pcntl
# pgsql
RUN apt-get install -y libpq-dev \
    && docker-php-ext-install pdo pdo_pgsql pgsql


RUN pecl install xdebug \
    && docker-php-ext-enable xdebug --ini-name 99-docker-php-ext-xdebug.ini

# memory_limit
RUN echo 'memory_limit = 512M' >> /usr/local/etc/php/conf.d/docker-php-memlimit.ini;

# Install composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer

RUN  curl -s -f -L -o /tmp/installer.php 'https://getcomposer.org/installer' \
    &&php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer \
    &&composer --ansi --version --no-interaction
# china packagist    
RUN composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
# pcd
RUN composer global require "squizlabs/php_codesniffer=*" -vvv
ENV PATH /code/vendor/bin:/composer/vendor/bin:$PATH
RUN php -m
# clean up our mess
RUN apt-get remove --purge -y software-properties-common && \
    apt-get autoremove -y && \
    apt-get clean && \
    apt-get autoclean && \
    echo -n > /var/lib/apt/extended_states && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/man/?? && \
    rm -rf /usr/share/man/??_*