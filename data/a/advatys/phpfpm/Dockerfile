FROM php:7.2.4-fpm

RUN apt-get update && apt-get install -y libpng-dev libjpeg-dev bzip2 && rm -rf /var/lib/apt/lists/*
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr 
RUN docker-php-ext-install gd mysqli opcache pdo pdo_mysql
RUN apt-get update && apt-get install -y libbz2-dev
RUN docker-php-ext-configure bz2 --with-bz2-dir=/bin
#RUN apt-get update && apt-get install -y php-dev 
RUN docker-php-ext-install exif zip
RUN apt-get update && apt-get install -y libxml2  
RUN docker-php-ext-install mbstring iconv fileinfo 
RUN apt-get update && apt-get install -y libxml2-dev
RUN docker-php-ext-install dom simplexml intl
RUN docker-php-ext-install bz2