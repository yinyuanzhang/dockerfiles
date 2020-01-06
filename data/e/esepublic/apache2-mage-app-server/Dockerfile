FROM esepublic/baseimage:0.9.16
MAINTAINER Keith Bentrup <kbentrup@ebay.com>

RUN add-apt-repository ppa:ondrej/php5-5.6 && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes apache2 \
    libapache2-mod-php5 \
    redis-tools \
    git \
    npm \
    ruby \
    php5-cli \
    php5-xdebug \
    php5-curl \
    php5-gd \
    php5-mcrypt \
    php-pear \
    php5-dev \
    php5-mysql \
    php5-intl \
    php5-xsl \
    unzip \
    mysql-client \
    libxml2-utils && \
  apt-get --purge autoremove -y && \
  apt-get clean && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*

# install mod_pagespeed
ADD https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-beta_current_amd64.deb /tmp/mod-pagespeed-beta_current_amd64.deb
RUN dpkg -i /tmp/mod-pagespeed-beta_current_amd64.deb && \
  apt-get -f install

# remove default sites, enable ssl, redis, rewrite, & mcrypt
RUN rm -rf /etc/apache2/sites-available/* /etc/apache2/sites-enabled/* && \
  mkdir -p /var/lock/apache2 /var/run/apache2 && \
  a2enmod ssl && \
  pecl install redis && \
  echo "extension=redis.so" > /etc/php5/mods-available/redis.ini && \
  php5enmod redis  && \
  ln -sf /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load

# install webgrind for profiling
ADD https://webgrind.googlecode.com/files/webgrind-release-1.0.zip /
RUN unzip /webgrind-release-1.0.zip -d / && \
  chown -R www-data:www-data /webgrind && \
  chmod -R g+w /webgrind

RUN curl -sS https://getcomposer.org/installer | php && \
  mv composer.phar /usr/local/bin/composer

COPY scripts /scripts
  
# runit apache2
RUN mkdir -p /etc/service/apache2 && \
  ln -sf /scripts/apache2.sh /etc/service/apache2/run

EXPOSE 80 443
