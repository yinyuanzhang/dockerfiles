FROM php:7.2.5

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

RUN apt-get update && apt-get install -my wget gnupg

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y xvfb libgtk-3-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2
RUN apt-get install -y unzip zip
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN apt-get install -qy git curl libmcrypt-dev mysql-client
RUN apt-get install -y libpng-dev
RUN apt-get install -y zlib1g-dev
RUN apt-get -yqq install exiftool
RUN docker-php-ext-configure exif
RUN docker-php-ext-install exif
RUN docker-php-ext-enable exif
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN docker-php-ext-install pdo_mysql 
RUN docker-php-ext-install gd
RUN docker-php-ext-install zip
RUN docker-php-ext-install bcmath
RUN docker-php-ext-install sockets
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g bower
RUN npm install -g gulp
RUN npm install -g grunt-cli
RUN apt-get install -y ruby-compass
RUN gem install compass sass-globbing
RUN apt-get install -y libmagickwand-dev --no-install-recommends
RUN pecl install imagick
RUN docker-php-ext-enable imagick
RUN pecl install xdebug-2.6.1
RUN docker-php-ext-enable xdebug
RUN cp -f /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime
RUN printf '[PHP]\ndate.timezone = "Europe/Amsterdam"\n' > /usr/local/etc/php/conf.d/tzone.ini
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install boto3==1.4.7

RUN docker-php-ext-configure pcntl --enable-pcntl
RUN docker-php-ext-install pcntl

RUN apt-get install -y libxml2-dev
RUN docker-php-ext-install soap

ADD s3_upload /usr/local/bin
RUN chmod u+x /usr/local/bin/s3_upload
