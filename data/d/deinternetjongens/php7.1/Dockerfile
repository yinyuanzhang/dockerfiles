FROM php:7.1.11

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && apt-get install -my wget gnupg

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y unzip zip
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN apt-get install -qy git curl libmcrypt-dev mysql-client
RUN apt-get install -y libpng-dev
RUN apt-get install -y zlib1g-dev
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN docker-php-ext-install mcrypt && docker-php-ext-install pdo_mysql
RUN docker-php-ext-install gd
RUN docker-php-ext-install zip
RUN docker-php-ext-install pcntl
RUN docker-php-ext-install calendar
RUN docker-php-ext-install bcmath && docker-php-ext-enable bcmath
RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++
RUN docker-php-ext-configure intl
RUN docker-php-ext-install intl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g bower
RUN npm install -g gulp
RUN apt-get install -y libmagickwand-dev --no-install-recommends
RUN pecl install imagick
RUN docker-php-ext-enable imagick
RUN pecl install pcov
RUN docker-php-ext-enable pcov
RUN cp -f /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime
RUN printf '[PHP]\ndate.timezone = "Europe/Amsterdam"\n' > /usr/local/etc/php/conf.d/tzone.ini
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install boto3==1.4.7

RUN apt-get install -y libxml2-dev
RUN docker-php-ext-install soap

ADD s3_upload /usr/local/bin
