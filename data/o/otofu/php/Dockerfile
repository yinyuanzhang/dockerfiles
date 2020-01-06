FROM php:7.3-apache

RUN set -ex \
 && apt update && apt -y upgrade \
 && apt install -y --no-install-recommends vim wget msmtp msmtp-mta git unzip default-mysql-client locales \
 && savedAptMark="$(apt-mark showmanual)" \
 && apt install -y --no-install-recommends libfreetype6-dev libjpeg62-turbo-dev libjpeg-dev libpng-dev libpq-dev libzip-dev libgmp-dev libssh2-1-dev libldap2-dev libicu-dev \
 && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
 && docker-php-ext-install -j "$(nproc)" gd opcache mysqli pdo_mysql pdo_pgsql zip gmp ldap intl \
 && pecl install xdebug && docker-php-ext-enable xdebug \
 && mkdir -p /usr/src/php/ext/uploadprogress \
 && up_url="https://github.com/wodby/pecl-php-uploadprogress/archive/latest.tar.gz" \
 && wget -qO- "${up_url}" | tar xz --strip-components=1 -C /usr/src/php/ext/uploadprogress \
 && docker-php-ext-install uploadprogress \
 && rm -rf /usr/src/php/ext/uploadprogress \
 && apt-mark auto '.*' > /dev/null \
 && apt-mark manual ${savedAptMark} \
 && ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \
    | awk '/=>/ { print $3 }' \
    | sort -u \
    | xargs -r dpkg-query -S \
    | cut -d: -f1 \
    | sort -u \
    | xargs -rt apt-mark manual \
 && apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*

RUN { \
  echo 'en_US.UTF-8 UTF-8'; \
  echo 'ja_JP.UTF-8 UTF-8'; \
} > /etc/locale.gen \
 && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN curl -sS https://getcomposer.org/installer | php \
 && mv composer.phar /usr/local/bin/composer \
 && chmod 755 /usr/local/bin/composer \
 && composer config -g repos.packagist composer https://packagist.jp \
 && composer global require hirak/prestissimo

ENV PATH ./vendor/bin:/root/.composer/vendor/bin/drush:${PATH}

RUN a2enmod rewrite vhost_alias

RUN { \
  echo 'opcache.enable=1'; \
  echo 'opcache.enable_cli=1'; \
  echo 'opcache.memory_consumption=128'; \
  echo 'opcache.interned_strings_buffer=8'; \
  echo 'opcache.max_accelerated_files=4000'; \
  echo 'opcache.revalidate_freq=60'; \
  echo 'opcache.fast_shutdown=1'; \
} > /usr/local/etc/php/conf.d/opcache-recommended.ini
