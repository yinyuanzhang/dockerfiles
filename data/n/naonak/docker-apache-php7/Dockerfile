FROM php:7-apache
MAINTAINER Fabien EVAIN <fevain@rmn.com>

## Install base packages

RUN apt-get update --fix-missing \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    php5-dev \
    php-pear \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libmcrypt-dev \
    libpng12-dev \
    libbz2-dev \
    libxslt-dev \
    libldap2-dev \
    libzmq-dev \
    git \
    unzip \
    locales \
    nano \
  && apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set system timezone
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

# Set system locale
RUN dpkg-reconfigure -f noninteractive locales \
  && echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen \
  && locale-gen

# PHP Extensions
RUN docker-php-ext-install -j$(nproc) zip bz2 xsl iconv mcrypt json mysqli opcache pdo pdo_mysql \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd \
  && docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \
  && docker-php-ext-install -j$(nproc) ldap

# Install apcu extension (data store only)
RUN pecl install apcu-5.1.5
RUN docker-php-ext-enable apcu

# Install mongodb extension
RUN pecl install mongodb-1.1.8
RUN docker-php-ext-enable mongodb

# Install redis extension
RUN pecl install redis
RUN docker-php-ext-enable redis

# Install zmq extension
RUN pecl install -f zmq-1.1.3
RUN docker-php-ext-enable zmq

## Apache
RUN cd /etc/apache2/sites-available/ && a2dissite *
ADD 000-default.conf /etc/apache2/sites-available/000-default.conf
ADD 010-site.conf /etc/apache2/sites-available/010-site.conf
RUN chmod 775 /etc/apache2/sites-available/*
RUN a2ensite 000-default 010-site

# Enable apache mods
RUN a2enmod rewrite
RUN a2enmod headers
RUN a2enmod deflate
RUN a2enmod expires
RUN a2enmod ssl

# Install apache2 conf
COPY apache2.conf /etc/apache2/apache2.conf

# Manually set up the apache environment variables
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_LOG_DIR /var/log/apache2

ENV APACHE_SERVERADMIN admin@localhost
ENV APACHE_SERVERNAME localhost
ENV APACHE_SERVERALIAS docker.localhost
ENV APACHE_DOCUMENTROOT /var/www

## Composer
# Based on https://github.com/RobLoach/docker-composer

# Register the COMPOSER_HOME environment variable
ENV COMPOSER_HOME /composer

# Add global binary directory to PATH and make sure to re-export it
ENV PATH /composer/vendor/bin:$PATH

# Allow Composer to be run as root
ENV COMPOSER_ALLOW_SUPERUSER 1

# Composer version
ENV COMPOSER_VERSION 1.2.0

# Setup the Composer installer
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \
  && curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \
  && php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !== trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }"

# Install composer
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-setup.php

## NodeJS, gulp, bower
# Based on https://github.com/nodejs/docker-node/blob/master/6.5/Dockerfile

# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 6.5.0

# Install NodeJS
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

ENV GULP_CLI_VERSION 1.2.2
ENV BOWER_VERSION 1.7.9

# Install globally gulp command line
RUN npm install --global gulp-cli@$GULP_CLI_VERSION

# Install globally bower command line
RUN npm install  --global bower@$BOWER_VERSION

## Finalize

# Define working directory
WORKDIR /var/www

# Expose some ports
EXPOSE 80

CMD ["apache2-foreground"]