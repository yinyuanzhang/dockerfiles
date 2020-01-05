FROM php:5.6-apache

EXPOSE 80

ENV PACKAGES="mysql-client ssmtp libjpeg62-turbo libpng-dev"
ENV BUILD_PACKAGES="default-libmysqlclient-dev wget libjpeg-dev libpq-dev"

ENV DRUPAL_VERSION 7.61
ENV DRUPAL_MD5 94bc49170d98e0cfe59db487911ecb9d

RUN . /etc/apache2/envvars && \
    apt-get update && \
    apt-get install -y  $PACKAGES $BUILD_PACKAGES && \
    docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \
    docker-php-ext-install gd mbstring pdo pdo_mysql zip && \
    pecl install uploadprogress && \
    docker-php-ext-enable uploadprogress opcache && \
    a2enmod rewrite && \
    wget "http://ftp.drupal.org/files/projects/drupal-${DRUPAL_VERSION}.tar.gz" -O drupal.tar.gz && \
    echo "${DRUPAL_MD5} *drupal.tar.gz" | md5sum -c - && \
    tar xf drupal.tar.gz -C /var/www/html --strip-components 1 && \
    rm drupal.tar.gz && \
    chown -R www-data:www-data sites && \
    apt-get autoremove --purge -y $BUILD_PACKAGES && \
    rm -rf /var/lib/apt/lists/*

ADD imagefiles /