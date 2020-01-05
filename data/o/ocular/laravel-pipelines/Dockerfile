FROM php:7.1-fpm-stretch

RUN apt-get update
RUN apt-get install -qy apt-utils
RUN apt-get upgrade -qy && apt-get install -qy git curl libmcrypt-dev mysql-client libxml2-dev zlib1g-dev gnupg unzip wget jq libfreetype6-dev libjpeg62-turbo-dev libpng-dev openssl libzip-dev
RUN wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb && dpkg -i /tmp/libpng12.deb && rm /tmp/libpng12.deb
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -qy nodejs
#RUN yes | pecl install mcrypt-1.0.2

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
RUN composer global require hirak/prestissimo

RUN docker-php-ext-install pdo_mysql
RUN docker-php-ext-install pcntl
RUN docker-php-ext-install zip
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install soap
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install gd

RUN git config --global user.email "pipelines@bitbucket.com"
RUN git config --global user.name "Pipelines Push"
