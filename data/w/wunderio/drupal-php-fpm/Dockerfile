# Based on php-fpm published by J.Petronetto, see LICENCE
FROM amazeeio/php:7.3-fpm

LABEL maintainer="wunder.io"
LABEL org.label-schema.name="Alpine with PHP7-FPM and Drush launcher" \
      org.label-schema.description="PHP7-FPM, common plugins and Drush laucher"

# Added due to https://github.com/drush-ops/drush/issues/4009  
RUN apk add --update --no-cache bash

# PHP modules and build dependencies
RUN apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS libtool imagemagick-dev openldap-dev libmemcached-dev \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && docker-php-ext-install ldap \
    && docker-php-ext-enable ldap \
    && yes '' | pecl install memcached \
    && docker-php-ext-enable memcached \
    && apk del .phpize-deps \
    && apk add --no-cache --virtual .imagick-runtime-deps imagemagick libmemcached

COPY config/ldap.conf /etc/openldap/ldap.conf

# Override Lagoon's entrypoint
COPY entrypoints/71-php-newrelic.sh /lagoon/entrypoints/

ENV DRUSH_LAUNCHER_VERSION=0.6.0

# Backwards-compatibility for projects using an older location.
RUN mkdir -p /var/www/html && ln -s /var/www/html /app

# Add gdpr-dump globally.
RUN apk add composer; \
     mkdir -p ~/.composer; \
     echo '{"minimum-stability": "dev"}' > ~/.composer/composer.json; \
     composer global require --prefer-dist machbarmacher/gdpr-dump:dev-master; \
     apk del composer

RUN set -ex; \
    # Install mysql client
    apk add mysql-client; \
    # Install GNU version of utilities
    apk add findutils coreutils; \
    # Install Drush launcher
    curl -OL https://github.com/drush-ops/drush-launcher/releases/download/${DRUSH_LAUNCHER_VERSION}/drush.phar; \
    chmod +x drush.phar; \
    mv drush.phar /usr/local/bin/drush; \
    \
    # Create directory for shared files
    mkdir -p -m +w /app/web/sites/default/files; \
    mkdir -p -m +w /app/private; \
    mkdir -p -m +w /app/reference-data; \
    chown -R www-data:www-data /app

WORKDIR /app/

# Add composer executables to our path.
ENV PATH="/app/vendor/bin:/home/.composer/vendor/bin:${PATH}"
