FROM php:5.6-fpm

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      bzip2 \
      sudo \
      git \
      libfreetype6-dev \
      libpng12-dev \
      libjpeg-dev \
      libmemcached-dev \
      libmcrypt-dev \
      mysql-client \
 && rm -rf /var/lib/apt/lists/* \
 && pecl install memcache \
 && docker-php-ext-enable memcache \
 && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir=/usr \
 && docker-php-ext-install \
      gd \
      zip \
      mysql \
      pdo_mysql \
      mcrypt \
      mbstring \
      json \
      gettext \
 && echo "date.timezone = 'UTC'" > /usr/local/etc/php/php.ini \
 && echo "short_open_tag = 0" >> /usr/local/etc/php/php.ini \
 && curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/usr/local/bin

ENV INSTALL_PATH=/var/www/html \
    VIMBADMIN_VERSION=3.0.15

RUN cd /tmp \
 && rm -rf $INSTALL_PATH \
 && curl -o VIMBADMIN.tar.gz -fSL https://github.com/opensolutions/ViMbAdmin/archive/${VIMBADMIN_VERSION}.tar.gz \
 && tar zxf VIMBADMIN.tar.gz \
 && rm VIMBADMIN.tar.gz \
 && mv ViMbAdmin-${VIMBADMIN_VERSION} $INSTALL_PATH \
 && cd $INSTALL_PATH \
 && composer install

WORKDIR /var/www/html
VOLUME /var/www/html
COPY mozilla-autoconfig.xml /var/www/html/public/mail/config-v1.1.xml
COPY mail.mobileconfig.php /var/www/html/public/mail.mobileconfig.php
COPY start.sh /usr/local/bin/start.sh
COPY application.ini /var/www/html/application/configs/application.ini

VOLUME /etc/nginx/conf.d
COPY nginx.conf /etc/nginx/conf.d/vimbadmin.conf

CMD ["/usr/local/bin/start.sh"]
