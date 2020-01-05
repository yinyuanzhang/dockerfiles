FROM php:7.0-cli
MAINTAINER Scott Murray <scott.murray@pushon.co.uk>

RUN apt-get update \
&& apt-get install -y \
cron \
libfreetype6-dev \
libicu-dev \
libjpeg62-turbo-dev \
libmcrypt-dev \
libpng12-dev \
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

RUN /bin/bash -c "curl -sL https://deb.nodesource.com/setup_7.x -o nodesource_setup.sh" && \
/bin/bash nodesource_setup.sh && \
apt-get install -y nodejs build-essential

RUN npm install -g bower grunt-cli && \
echo '{ "allow_root": true }' > /root/.bowerrc

RUN curl -sS https://getcomposer.org/installer | \
  php -- --install-dir=/usr/local/bin --filename=composer

RUN composer global require deployer/deployer ~4.3.0
RUN composer global require "hirak/prestissimo:^0.3"