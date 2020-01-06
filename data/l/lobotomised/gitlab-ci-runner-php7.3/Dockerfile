FROM php:7.3-stretch

ENV PHP_USER=php
ENV HOME=/home/$PHP_USER DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp

#
# Configuration initial
#
RUN sed 's|deb.debian.org|ftp.fr.debian.org|g' -i /etc/apt/sources.list \
&&  sed 's|security.debian.org|ftp.fr.debian.org|g' -i /etc/apt/sources.list \
&&  sed 's|deb.debian.org|ftp.fr.debian.org|g' -i /etc/apt/sources.list.d/buster.list \
# On a pas besoin du cache d'apt dans un container
&&  echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache \
&&  echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf

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

#
# Extention php
#
RUN apt-get install -yqq --no-install-recommends \
      default-libmysqlclient-dev \
      libbz2-dev \
      libfreetype6-dev \
      libicu-dev \
      libjpeg-dev \
      libmagickwand-dev \
      libpng-dev \
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
      pdo_pgsql \
      pgsql \
      soap \
      xmlrpc \
      zip \
&&  docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
&&  docker-php-ext-install gd \
&&  pecl channel-update pecl.php.net \
&&  pecl upgrade \
&&  pecl install redis imagick \
&&  pecl install xdebug \
&&  docker-php-ext-enable xdebug \
&&  docker-php-ext-enable redis imagick \
&&  docker-php-source delete \
{ \
      echo 'opcache.enable=1'; \
      echo 'opcache.revalidate_freq=0'; \
      echo 'opcache.validate_timestamps=1'; \
      echo 'opcache.max_accelerated_files=10000'; \
      echo 'opcache.memory_consumption=192'; \
      echo 'opcache.max_wasted_percentage=10'; \
      echo 'opcache.interned_strings_buffer=16'; \
      echo 'opcache.fast_shutdown=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/zz-conf.ini \
&&  curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
&&  chown -R $PHP_USER:$PHP_USER $HOME \
&&  su $PHP_USER -c 'composer global require "hirak/prestissimo:^0.3"' \
&&  su $PHP_USER -c 'composer global require "laravel/envoy=~1.0"' \
&&  rm -rf ~/.composer/cache/* \
&&  mkdir -p /var/www/html \
&&  chown -R $PHP_USER:$PHP_USER /var/www/html

#
# Node.js npm & yarn
#
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
&&  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
&&  curl -sL https://deb.nodesource.com/setup_12.x | bash - \
&&  apt-get install nodejs yarn -yqq \
&&  npm install --global npm \
&&  npm cache clean --force \
&&  chown -R $PHP_USER:$PHP_USER $HOME/.npm \
&&  chown -R $PHP_USER:$PHP_USER $HOME/.config

#
# Cleanup
#
RUN rm -rf /usr/lib/node_modules/ \
&&  apt-get purge -yqq --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o APT::AutoRemove::SuggestsImportant=false \
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

USER $PHP_USER

WORKDIR /var/www/html
