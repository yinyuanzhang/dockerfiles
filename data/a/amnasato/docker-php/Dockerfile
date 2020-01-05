FROM php:7.1-fpm-alpine

# install and configure PHP extensions
RUN set -ex; \
   apk add --no-cache jpeg-dev libpng-dev; \
   docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
   docker-php-ext-install gd mysqli opcache;

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
     echo 'opcache.memory_consumption=128'; \
     echo 'opcache.interned_strings_buffer=8'; \
     echo 'opcache.max_accelerated_files=4000'; \
     echo 'opcache.revalidate_freq=2'; \
     echo 'opcache.fast_shutdown=1'; \
     echo 'opcache.enable_cli=1'; \
  } > /usr/local/etc/php/conf.d/opcache-recommended.ini

# Configure php-fmp
RUN echo $'[www]\naccess.format = "[%t] %u \\"%m %r%Q%q\\" %s %f %{mili}dms %{kilobytes}MkB %C%%"' > /usr/local/etc/php-fpm.d/access.conf

#install composer
RUN set -ex; \
    apk add --no-cache git zip; \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer;

WORKDIR /var/www/html
