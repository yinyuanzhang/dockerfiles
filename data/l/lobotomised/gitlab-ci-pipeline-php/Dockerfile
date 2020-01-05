FROM php:7.4-buster

ENV PHP_USER=php
ENV HOME=/home/$PHP_USER DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

# Création de l'utilisateur de php
RUN adduser --disabled-password --gecos '' $PHP_USER \
&&  echo "$PHP_USER ALL = ( ALL ) NOPASSWD: ALL" >> /etc/sudoer \
&&  chown -R $PHP_USER:$PHP_USER /var/www $HOME

RUN apt-get update && apt-get install -yqq --no-install-recommends \
      apt-transport-https \
      autoconf \
      build-essential \
      ca-certificates \
      dpkg-dev \
      file \
      g++ \
      gcc \
      git \
      gnupg2 \
      libc-dev \
      libc-client-dev \
      lsb-release \
      make \
      openssl \
      openssh-client \
      pkg-config \
      python \
      python-dev \
      re2c \
      rsync \
      sudo \
      xz-utils \
      unzip \
      zip \
      zlib1g-dev

RUN apt-get install -yqq --no-install-recommends \
      default-libmysqlclient-dev \
      libbz2-dev \
      libfreetype6-dev \
      libicu-dev \
      libpq-dev \
      libsasl2-dev \
      libssl-dev \
      libxml2-dev \
      libzip-dev\
&&  docker-php-ext-install \
      bcmath \
      bz2 \
      calendar \
      exif \
      intl \
      mysqli \
      opcache \
      pcntl \
      pdo_mysql \
      pgsql \
      soap \
      xmlrpc \
      zip \
&&  pecl channel-update pecl.php.net \
&&  pecl upgrade \
&&  pecl install redis \
&&  pecl install xdebug \
&&  docker-php-ext-enable xdebug \
&&  docker-php-ext-enable redis \
&&  docker-php-source delete \
&&  echo 'opcache.enable=1'; >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.revalidate_freq=0' >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.validate_timestamps=1' >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.max_accelerated_files=10000' >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.memory_consumption=192' >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.max_wasted_percentage=10' >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.interned_strings_buffer=16' >> /usr/local/etc/php/conf.d/opcache-recommended.ini \
&&  echo 'opcache.fast_shutdown=1' >> /usr/local/etc/php/conf.d/opcache-recommended.ini

ENV COMPOSER_HOME=/composer
ENV PATH=./vendor/bin:/composer/vendor/bin:/root/.yarn/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV COMPOSER_ALLOW_SUPERUSER=1
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
&&  composer global require "hirak/prestissimo:^0.3" "laravel/envoy:^1.0"

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
&& apt-get install -y nodejs

RUN  apt-get purge -yqq --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false \
      apt-transport-https \
      autoconf \
      build-essential \
      dpkg-dev \
      file \
      g++ \
      gcc \
      gnupg2 \
      libc-dev \
      libc-client-dev \
      lsb-release \
      libsasl2-dev \
      make \
      python-dev \
      re2c \
      rsync \
      xz-utils \
# nettoyage de l'index
&&  apt-get autoremove -yqq --purge \
&&  apt-get autoclean -yqq \
&&  apt-get clean \
# supprime tout ce qui est inutile
&&  rm -rf /var/cache/apt/ \
      /tmp/* \
      /var/lib/apt/lists/* \
      /var/log/* \
      /var/tmp/* \
      /usr/share/doc \
      /usr/share/doc-base \
      /usr/share/gnome/help/*/* \
      /usr/share/groff/* \
      /usr/share/info/* \
      /usr/share/linda/* \
      /usr/share/lintian/overrides/* \
      /usr/share/locale/* \
      /usr/share/man/* \
      /usr/share/omf/*/*-*.emf

WORKDIR /var/www/html
