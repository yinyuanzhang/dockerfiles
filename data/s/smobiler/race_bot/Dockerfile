FROM php:7.0-apache

ENV PHP_EXT_APCU_VERSION "5.1.7"
ENV PHP_EXT_MEMCACHED_VERSION "3.0.3"

RUN build_packages="libmcrypt-dev libfreetype6-dev libjpeg62-turbo-dev libxml2-dev libxslt1-dev libmemcached-dev sendmail-bin sendmail libicu-dev imagemagick libmagickwand-dev" \
    && apt-get update && apt-get install -y $build_packages \
    && apt-get install -y nano mc htop pv wget apt-utils varnish \
    && yes "" | pecl install apcu-$PHP_EXT_APCU_VERSION && docker-php-ext-enable apcu \
    && yes "" | pecl install imagick && docker-php-ext-enable imagick \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install mcrypt \
    && echo "no" | pecl install memcached-$PHP_EXT_MEMCACHED_VERSION && docker-php-ext-enable memcached \
    && docker-php-ext-install pcntl \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install soap \
    && docker-php-ext-install xsl \
    && docker-php-ext-install zip \
    && docker-php-ext-install intl \
    && docker-php-ext-install sockets \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


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


# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
        echo "alias composer='composer'" >> /root/.bashrc \
        && composer


# Put apache config
COPY build/custom-vhost.conf /etc/apache2/sites-available/custom-vhost.conf

RUN mkdir /var/www/html/web
RUN touch /var/www/html/web/index.php

RUN a2dissite 000-default.conf
RUN a2ensite custom-vhost.conf
RUN a2enmod rewrite expires headers deflate remoteip


# Change uid and gid of apache to docker user uid/gid
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data

ENV BIN_DIR "/usr/local/bin"

RUN service apache2 restart

WORKDIR /var/www/html

# COPY build/docker-entrypoint.sh /
# RUN chmod +x /docker-entrypoint.sh
# CMD ["/docker-entrypoint.sh"]

