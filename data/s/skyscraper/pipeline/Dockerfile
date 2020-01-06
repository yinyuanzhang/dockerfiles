FROM php:7.3-fpm

RUN apt-get update -y \
    && apt-get install -y libxml2-dev libicu-dev zlib1g-dev libzip-dev mysql-client git openssh-client \
        libfreetype6-dev libjpeg62-turbo-dev libxpm-dev libpng-dev \
        ffmpeg \
    && docker-php-source extract \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ --with-xpm-dir=/usr/include/ --enable-gd-jis-conv \
    && docker-php-ext-install zip mbstring dom bcmath intl pdo_mysql gd exif sockets \
    && docker-php-source delete

RUN curl -OL https://github.com/jwilder/dockerize/releases/download/v0.6.0/dockerize-linux-amd64-v0.6.0.tar.gz && tar --skip-old-files -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.0.tar.gz && rm dockerize-linux-amd64-v0.6.0.tar.gz
# Install Composer and make it available in the PATH
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

## Install Node.js
RUN apt-get install -y gnupg gnupg1 gnupg2 \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs
