FROM php:5.6-apache

# PHP extensions we need
RUN apt-get update && apt-get install -y \
    libmemcached-dev \
    uuid-dev \
    zlib1g-dev \
    acl \
    libzip-dev \
    libicu-dev \
    unzip \
    libxml2-dev \
    libtidy-dev \
    graphicsmagick \
  && rm -rf /var/lib/apt/lists/* \
  && docker-php-ext-configure intl \
  && docker-php-ext-configure zip \
  && docker-php-ext-install \
    zip \
    intl \
    mysqli \
    pdo_mysql \
    opcache \
    pcntl \
    sockets \
    soap \
    tidy \
    bcmath

# Pecl
RUN pecl install igbinary-2.0.8 uuid memcache

RUN pecl install --nobuild memcached-2.2.0 && \
            cd "$(pecl config-get temp_dir)/memcached" && \
            phpize && \
            ./configure --enable-memcached-igbinary && \
            make -j$(nproc) && \
            make install

RUN docker-php-ext-enable memcache memcached uuid igbinary

# Cleanup
RUN apt-get update && apt-get purge -y --auto-remove uuid-dev libmemcached-dev \
    && apt-get install -y libmemcached11 libmemcachedutil2 \
    --no-install-recommends \
    && apt-get clean && apt-get autoremove -q \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/share/doc /usr/share/man /tmp/*

# Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer

ENV PATH="/home/readitla/vendor/bin:${PATH}"

# GeoIP
RUN mkdir -p ./tmp
ADD http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz ./tmp/
RUN tar -xvf ./tmp/GeoLite2-City.tar.gz -C /usr/local/share \
    && mv /usr/local/share/Geo*2-City_20*/*.mmdb /usr/local/share/GeoIP2-City.mmdb \
    && rm -r /usr/local/share/Geo*2-City_20* ./tmp

# Download Browscap ini file
RUN mkdir -p /usr/local/etc/php/extra/ \
    && curl "http://browscap.org/stream?q=Full_PHP_BrowsCapINI" -o /usr/local/etc/php/extra/full_php_browscap.ini

# Setup paths
RUN mkdir -p /home/readitla

# Setup apache
COPY ./httpd-web-app.conf $APACHE_CONFDIR/sites-available/httpd-web-app.conf
COPY ./httpd-server-status.conf $APACHE_CONFDIR/sites-available/httpd-server-status.conf

RUN a2ensite httpd-web-app
RUN a2ensite httpd-server-status
RUN a2dissite 000-default
RUN a2enmod rewrite expires headers remoteip

WORKDIR /home/readitla


CMD ["apache2-foreground"]
