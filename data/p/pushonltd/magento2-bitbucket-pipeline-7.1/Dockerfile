FROM php:7.1-cli
MAINTAINER Scott Murray <scott.murray@pushon.co.uk>

RUN apt-get update \
&& apt-get install -y \
cron \
libfreetype6-dev \
libicu-dev \
libjpeg62-turbo-dev \
libmcrypt-dev \
libpng-dev \
libxslt1-dev \
git

RUN docker-php-ext-configure \
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/

RUN docker-php-ext-install \
gd \
intl \
mbstring \
mcrypt \
pdo_mysql \
soap \
xsl \
zip \
bcmath

RUN apt-get install -y gpg

RUN /bin/bash -c "curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh" && \
/bin/bash nodesource_setup.sh && \
apt-get install -y nodejs build-essential

RUN npm install -g bower grunt-cli && \
echo '{ "allow_root": true }' > /root/.bowerrc

RUN npm install gulp-cli -g && npm install gulp -D

RUN curl -sS https://getcomposer.org/installer | \
  php -- --install-dir=/usr/local/bin --filename=composer

RUN composer global require deployer/deployer
RUN composer global require "hirak/prestissimo"

# Ioncube
RUN curl -o ioncube_loaders_lin_x86-64.tar.gz http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz \
        && tar xfz ioncube_loaders_lin_x86-64.tar.gz \
        && cp ioncube/ioncube_loader_lin_7.1.so /usr/local/lib/php/extensions/no-debug-non-zts-20160303/ \
        && echo "zend_extension=ioncube_loader_lin_7.1.so" > /usr/local/etc/php/conf.d/00_docker-php-ext-ioncube_loader_lin_7.1.ini \
        && rm -Rf ioncube_loaders_lin_x86-64.tar.gz ioncube
