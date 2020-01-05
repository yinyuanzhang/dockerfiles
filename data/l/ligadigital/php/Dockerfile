FROM php:7.1-apache

LABEL Name=php Version=7.1-catwalk

WORKDIR /srv

ENV APACHE_DOCUMENT_ROOT /srv/web
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

ENV DEBIAN_FRONTEND=noninteractive
RUN  \
      apt-get update && \
      apt-get install -y \
        apt-utils \
        debian-archive-keyring \
        dialog \
        expect-dev \
        ghostscript \
        git\
        gnupg \
        libcurl3-gnutls\
        libfreetype6-dev \
        libgeoip-dev \
        libgmp-dev \
        libgs9-common \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        locales \
        mariadb-client \
        openssl \
        python \
        software-properties-common \
        unoconv \
        unzip \
        wget \
        wkhtmltopdf \
        zip \
        zlib1g-dev \
        && \
      ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install -j$(nproc) \
      bcmath \
      gd \
      gmp \
      iconv \
      mbstring \
      mcrypt \
      mysqli \
      pdo \
      pdo_mysql \
      sockets \
      zip \
      && \
    pecl install apcu apcu_bc && \
    docker-php-ext-enable apcu apc && \
    a2enmod rewrite && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN a2enmod rewrite

RUN mv /usr/local/etc/php/conf.d/docker-php-ext-apc.ini /usr/local/etc/php/conf.d/zz-docker-php-ext-apc.ini

# Install composer
RUN  mkdir bin \
  && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php composer-setup.php --install-dir=/usr/local/bin  \
  && php -r "unlink('composer-setup.php');"

# Allow composer to be run as root
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV QT_QPA_PLATFORM=offscreen

