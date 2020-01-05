# PHP 7.2 Appserver with select extensions, composer and Platform.sh CLI tool.

# Build extensions using the official PHP Debian (buster) image.
FROM php:7.2-fpm-buster as build

# Install build dependencies, build and install extensions.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libbz2-dev \
    libfreetype6-dev \
    libicu-dev \
    libjpeg-dev \
    libpng-dev \
    libxml2-dev \
    libzip-dev \
  && pecl install apcu \
  && pecl install igbinary \
  && pecl install redis-3.1.2 \
  && pecl install xdebug \
  && docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr --with-jpeg-dir=/usr \
  && docker-php-ext-configure zip --with-libzip \
  && docker-php-ext-enable apcu \
  && docker-php-ext-enable igbinary \
  && docker-php-ext-enable redis \
  && docker-php-ext-enable xdebug \
  && docker-php-ext-install \
    bcmath \
    bz2 \
    calendar \
    exif \
    gd \
    mysqli \
    opcache \
    pdo_mysql \
    soap \
    zip \
    intl \
    gettext \
    pcntl \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /tmp/* \
  && find "$(php -r 'echo ini_get("extension_dir");')" -type f -executable -exec strip --strip-all '{}' +

FROM debian:buster-slim

# Install runtime dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends \
    bzip2 \
    ca-certificates \
    curl \
    default-mysql-client \
    git-core \
    libargon2-1 \
    libedit2 \
    libfreetype6 \
    libicu63 \
    libjpeg62-turbo \
    libpng16-16 \
    libsodium23 \
    libsqlite3-0 \
    libssl1.1 \
    libxml2 \
    libzip4 \
    openssh-client \
    patch \
    rsync \
    unzip \
    wget \
    xfonts-base \
    xfonts-75dpi \
    xz-utils \
  && rm -rf /var/lib/apt/lists/*

# Copy apt configuration from PHP build image.
COPY --from=build /etc/apt/preferences.d/no-debian-php /etc/apt/preferences.d/no-debian-php

# Copy php, php-fpm, extensions and their config from PHP build image.
COPY --from=build /usr/local/bin/php /usr/local/bin/php
COPY --from=build /usr/local/sbin/php-fpm /usr/local/sbin/php-fpm
COPY --from=build /usr/local/lib/php /usr/local/lib/php
COPY --from=build /usr/local/etc/php /usr/local/etc/php
COPY --from=build /usr/local/etc/php-fpm.conf /usr/local/etc/php-fpm.conf
COPY --from=build /usr/local/etc/php-fpm.d /usr/local/etc/php-fpm.d

ENV PHP_INI_DIR /usr/local/etc/php
ENTRYPOINT ["docker-php-entrypoint"]
STOPSIGNAL SIGQUIT
EXPOSE 9000
CMD ["php-fpm"]

# Copy customised entrypoint.
COPY docker-php-entrypoint /usr/local/bin/docker-php-entrypoint

WORKDIR /usr/local/etc/php

# Set up PHP configuration using our custom overrides.
COPY php-*.ini /tmp/

RUN cat php.ini-development /tmp/php-common.ini > php.ini \
  && cat php.ini /tmp/php-cli.ini > php-cli.ini \
  && mkdir xdebug \
  && cat php.ini /tmp/php-xdebug.ini > xdebug/php.ini \
  && cat php-cli.ini /tmp/php-xdebug.ini > xdebug/php-cli.ini \
  && rm /tmp/php-*.ini \
  && rm /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
  && rm /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
  && mkdir -p /var/cache/php \
  && chown -R www-data:www-data /var/cache/php

# Install composer.
COPY install_composer.sh /install_composer.sh
RUN /install_composer.sh; rm /install_composer.sh

# Set up web user's home directory and install prestissimo.
RUN chsh -s /bin/bash www-data \
  && mkdir -p /var/www/.composer \
  && chown -R www-data:www-data /var/www \
  && su -c "composer global require hirak/prestissimo" -s /bin/sh www-data \
  && rm -rf /var/www/.composer/cache

# Install mhsendmail binary.
RUN curl -fsSL -o /usr/local/bin/mhsendmail https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 \
 && chmod +x /usr/local/bin/mhsendmail

# Create mount points for app code and files, owned by the web server.
RUN mkdir -p /app/private /app/web/files \
  && chown -R www-data:www-data /app

USER www-data
WORKDIR /app

# Install Platform.sh cli tool, requires a shell config file.
RUN touch /var/www/.bashrc \
  && curl -sS https://platform.sh/cli/installer | php \
  && rm /var/www/.bashrc.cli.bak

COPY --chown=www-data:www-data platform-cli.config.yaml /var/www/.platformsh/config.yaml

ENV PATH /var/www/.platformsh/bin:/app/vendor/bin:$PATH
