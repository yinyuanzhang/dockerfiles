FROM php:7.1-apache

RUN apt-get update && apt-get install -y \
    zlib1g-dev \
    libicu-dev \
    g++ \
    libssl-dev \
    apt-transport-https

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/8/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update

RUN ACCEPT_EULA=Y apt-get install -y \
  libcurl4-openssl-dev \
  sudo \
  git \
  vim \
  libxslt-dev \
  graphviz \
  zip \
  libmcrypt-dev \
  libpcre3-dev \
  libgd-dev \
  libfreetype6-dev \
  libgmp-dev \
  mysql-client \
  libgeoip-dev \
  unixodbc \
  unixodbc-dev \
  odbcinst \
  msodbcsql \
  locales \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

RUN apt-get clean

RUN docker-php-ext-install \
  soap \
  gmp \
  dom \
  bcmath \
  zip \
  xsl \
  mcrypt \
  mbstring \
  gettext \
  curl \
  pdo_mysql \
  json \
  intl \
  opcache \
  mysqli \
  calendar

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/ \
  && docker-php-ext-install gd

RUN pecl install xdebug \
  && docker-php-ext-enable xdebug \
  && { \
     		echo "xdebug.remote_enable=On"; \
     		echo "xdebug.remote_connect_back=On"; \
     	} | tee -a /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

RUN pecl install geoip-1.1.1 \
	&& echo "extension=geoip.so" > /usr/local/etc/php/conf.d/ext-geoip.ini

RUN pecl install gender \
    && docker-php-ext-enable gender

RUN pecl install pdo_sqlsrv && \
    echo -e "extension=pdo_sqlsrv.so" > /usr/local/etc/php/conf.d/ext-pdosqlsrv.ini && \
    docker-php-ext-enable pdo_sqlsrv

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN a2enmod rewrite
RUN usermod -u 1000 www-data
