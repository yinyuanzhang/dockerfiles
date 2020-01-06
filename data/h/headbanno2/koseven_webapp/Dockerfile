FROM php:7.1-apache


ENV KOHANA_ENV=""
ENV APPLICATION_ENV production
ENV KOSEVEN_TIME_ZONE="America/New_York"



# =============================================================================
# FROM: https://github.com/blankoworld/docker-makefly/blob/master/Dockerfile
# =============================================================================
# Get noninteractive frontend for Debian to avoid some problems:
#    debconf: unable to initialize frontend: Dialog
ENV DEBIAN_FRONTEND noninteractive



# =============================================================================
# Ensure UTF-8 and locale is set
# FROM:
#  - https://github.com/blankoworld/docker-makefly/blob/master/Dockerfile
#  - https://github.com/GM-Alex/docker-phpapp/blob/master/Dockerfile
#  - https://github.com/fideloper/docker-nginx-php/blob/master/Dockerfile
#  - https://github.com/sinso/docker-phpfpm-typo3/blob/master/Dockerfile
#  - https://github.com/iserko/docker-ubuntu-locale/blob/master/Dockerfile
# =============================================================================
RUN apt-get update \
  && apt-get install -y locales \
  && dpkg-reconfigure locales \
  && locale-gen C.UTF-8 \
  && /usr/sbin/update-locale LANG=C.UTF-8 \
  && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
  && locale-gen

# Set default locale for the environment
ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8



# =============================================================================

# Fix docker-php-ext-install script error
RUN sed -i 's/docker-php-\(ext-$ext.ini\)/\1/' /usr/local/bin/docker-php-ext-install

RUN pear config-set php_ini /usr/local/etc/php/php.ini
RUN pecl config-set php_ini /usr/local/etc/php/php.ini

# Install other needed extensions
RUN apt-get update \
  && apt-get install -y \
    libfreetype6 \
    libjpeg62-turbo \
    libmcrypt4 \
    libpng12-0 \
    sendmail \
    curl \
    git \
    subversion \
    unzip \
    wget \
    mysql-client \
    --no-install-recommends

RUN apt-get update && apt-get install -y \
  libfreetype6-dev \
  libjpeg62-turbo-dev \
  libjpeg-dev \
  libldap2-dev \
  libpng12-dev \
  libmcrypt-dev \
  libpng12-dev \
  zlib1g-dev \
  libbz2-dev \
  libxslt-dev \
  libmemcached-dev \
  libcurl4-openssl-dev \
  --no-install-recommends



# =============================================================================
# Install needed php extensions: ldap
# https://github.com/docker-library/php/issues/75#issuecomment-82075678
# =============================================================================
RUN \
    apt-get update && \
    apt-get install libldap2-dev -y && \
    rm -rf /var/lib/apt/lists/* && \
    docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \
    docker-php-ext-install ldap



RUN docker-php-ext-configure gd \
      --enable-gd-native-ttf \
      --with-jpeg-dir=/usr/lib/x86_64-linux-gnu \
      --with-png-dir=/usr/lib/x86_64-linux-gnu \
      --with-freetype-dir=/usr/lib/x86_64-linux-gnu \
  && docker-php-ext-install gd \
  && docker-php-ext-install curl \
  && docker-php-ext-install mysqli \
  && docker-php-ext-install mcrypt \
  && docker-php-ext-install pdo \
  && docker-php-ext-install pdo_mysql \
  && docker-php-ext-install soap \
  && docker-php-ext-install opcache



# =============================================================================
# Install memcached
# https://stackoverflow.com/a/39348230
# =============================================================================
RUN apt-get update && apt-get install -y \
        libmemcached11 \
        libmemcachedutil2 \
        libmemcached-dev \
        libz-dev \
        git \
    && cd /root \
    && git clone -b php7 https://github.com/php-memcached-dev/php-memcached \
    && cd php-memcached \
    && phpize \
    && ./configure \
    && make \
    && make install \
    && cd .. \
    && rm -rf  php-memcached \
    && echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini \
    && apt-get remove -y build-essential libmemcached-dev libz-dev \
    && apt-get remove -y \
        libmemcached-dev \
        libz-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean



# =============================================================================
# https://github.com/RobLoach/docker-composer/blob/master/base/php5/Dockerfile
# =============================================================================

# Memory Limit
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini

# Time Zone
ENV PHP_TIMEZONE $KOSEVEN_TIME_ZONE
RUN echo "date.timezone=${PHP_TIMEZONE}" > $PHP_INI_DIR/conf.d/date_timezone.ini

# Register the COMPOSER_HOME environment variable
ENV COMPOSER_HOME /composer

# Add global binary directory to PATH and make sure to re-export it
ENV PATH /composer/vendor/bin:$PATH

# Allow Composer to be run as root
ENV COMPOSER_ALLOW_SUPERUSER 1

# Setup the Composer installer
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \
  && curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \
  && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }"



# =============================================================================
# https://github.com/RobLoach/docker-composer/blob/master/1.1/php5/Dockerfile
# =============================================================================

ENV COMPOSER_VERSION 1.1.2

# Install Composer
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-setup.php



# =============================================================================
# FROM: https://github.com/JulienBreux/phpunit-docker/blob/master/4.8.16/Dockerfile
# =============================================================================

# Goto temporary directory.
WORKDIR /tmp

# Run composer and phpunit installation.
RUN composer selfupdate && \
    composer require "phpunit/phpunit:5.7.27" --prefer-source --no-interaction && \
    ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit



# =============================================================================
RUN apt-get autoremove -y && apt-get clean all



# =============================================================================
RUN echo $KOSEVEN_TIME_ZONE > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata



# =============================================================================
# ADD https://curl.haxx.se/ca/cacert.pem /etc/ssl/certs/
ADD cacert.pem /etc/ssl/certs/



# =============================================================================
RUN a2enmod rewrite



# =============================================================================
# Goto temporary directory.
WORKDIR /var/www/html



# =============================================================================
ENV TERM="xterm"



# =============================================================================
# Run test as same user as apache is running
# FROM: http://stackoverflow.com/a/25908200
# =============================================================================
RUN apt-get update
RUN apt-get -y install sudo


# Move to main php ext installation loop
RUN apt-get update \
  && apt-get install -y libssl-dev \
  && rm -rf /var/lib/apt/lists/* \
  && docker-php-ext-install ftp

VOLUME /composer
VOLUME /var/www/uploads
VOLUME /var/log/apache2
VOLUME /var/www/html/application/cache
VOLUME /var/www/html/application/logs
VOLUME /var/www/html/application/tests/logs
