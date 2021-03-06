FROM php:7.3-apache

ENV APACHE_DOCUMENT_ROOT /var/www/web
ENV NODE_MAJOR_VERSION 11

ENV PATH="/var/www/vendor/bin:${PATH}"

# Install dependencies
RUN set -ex; \
  \
  mkdir -p /usr/share/man/man1 /usr/share/man/man7; \
  \
  if command -v a2enmod; then \
    a2enmod rewrite; \
  fi; \
  \
  savedAptMark="$(apt-mark showmanual)"; \
  \
  # install the installation dependencies we need
  apt-get update; \
  apt-get install -y --no-install-recommends \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    libzip-dev \
    gnupg \
  ; \
  \
  # install the PHP extensions we need
  docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
  docker-php-ext-install -j "$(nproc)" \
    gd \
    opcache \
    pdo_mysql \
    pdo_pgsql \
    zip \
  ; \
  \
  # reset apt-mark's "manual" list so that "purge --auto-remove" will remove all build dependencies
  apt-mark auto '.*' > /dev/null; \
  apt-mark manual $savedAptMark; \
  ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
    | awk '/=>/ { print $3 }' \
    | sort -u \
    | xargs -r dpkg-query -S \
    | cut -d: -f1 \
    | sort -u \
    | xargs -rt apt-mark manual; \
  \
  # install running dependencies
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - ; \
  echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list; \
  \
  curl -sL https://deb.nodesource.com/setup_${NODE_MAJOR_VERSION}.x | bash - ; \
  \
  apt-get update; \
  apt-get install -y --no-install-recommends \
    cron \
    git \
    mysql-client \
    nodejs \
    python2.7 \
    unzip \
    vim \
    yarn \
  ; \
  \
  apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
  rm -rf /var/lib/apt/lists/*

# setup apache
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
    echo 'opcache.memory_consumption=128'; \
    echo 'opcache.interned_strings_buffer=8'; \
    echo 'opcache.max_accelerated_files=4000'; \
    echo 'opcache.revalidate_freq=60'; \
    echo 'opcache.fast_shutdown=1'; \
    echo 'opcache.enable_cli=1'; \
  } > /usr/local/etc/php/conf.d/opcache-recommended.ini

# setup npm
RUN npm config set --global python python2.7

# setup cron
RUN touch /var/log/cron.log

# install Composer.
RUN curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

# install custom scripts
COPY ./scripts/docker-as-* /usr/local/bin/

# set workdir and volume
RUN rm -rf /var/www/*
WORKDIR /var/www

VOLUME /var/www

ENTRYPOINT ["docker-as-entrypoint"]
CMD ["apache2-foreground"]
