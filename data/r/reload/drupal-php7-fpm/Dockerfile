FROM phusion/baseimage:0.11

ENV PHP_VERSION 7.3

# Basic package installation
RUN \
  # Add a repo that contains php ${PHP_VERSION}
  LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \
  install_clean \
      php${PHP_VERSION}-fpm \
      php${PHP_VERSION}-curl \
      php${PHP_VERSION}-gd \
      php${PHP_VERSION}-xml \
      php${PHP_VERSION}-mysql \
      php${PHP_VERSION}-mbstring \
      php-xdebug \
      php${PHP_VERSION}-soap \
      php${PHP_VERSION}-sqlite3 \
      php${PHP_VERSION}-zip \
      php${PHP_VERSION}-intl \
      php${PHP_VERSION}-bcmath \
      php-imagick \
      php-memcache \
      php-memcached \
      # Mysql-client added to support eg. drush sqlc
      mysql-client \
      # Git and unzip are required by composer
      git \
      unzip \
      wget \
      dnsutils \
      curl \
      iputils-ping \
      telnet \
      imagemagick \
      patch

# We disable xdebug pr default and leave it up to the user of the image to
# enable at runtime. We disable it right away so that composer used in a
# later step runs a bit faster.
RUN phpdismod xdebug

# Add the blackfire repo and install the php-probe.
# We also fetch the blackfire-agent to get access to the commandlineuploader.
RUN \
  wget -O - https://packages.blackfire.io/gpg.key | apt-key add - && \
  echo "deb http://packages.blackfire.io/debian any main" | tee /etc/apt/sources.list.d/blackfire.list && \
  install_clean blackfire-php blackfire-agent

# Setup fpm paths and log
RUN \
  mkdir /run/php/ && \
  chown www-data:www-data /run/php/ && \
  touch /var/log/fpm-php.www.log && \
  chown www-data:www-data /var/log/fpm-php.www.log

# Install composer 1.6.5  using the latest installer.
# We compare the downloaded installer with a hash from a second source to reduce
# the chanche we're downloading a compromised installer.
RUN curl -o /tmp/composer-installer https://getcomposer.org/installer && \
  curl -o /tmp/composer-installer.sig https://composer.github.io/installer.sig &&  \
  php -r "if (hash('SHA384', file_get_contents('/tmp/composer-installer')) !== trim(file_get_contents('/tmp/composer-installer.sig'))) { unlink('/tmp/composer-installer'); echo 'Invalid installer' . PHP_EOL; exit(1); }" && \
  php /tmp/composer-installer --version=1.6.5 --filename=composer --install-dir=/usr/local/bin && \
  php -r "unlink('/tmp/composer-installer');" && \
  php -r "unlink('/tmp/composer-installer.sig');" && \
  composer global require "hirak/prestissimo:^0.3"

# Add cgr as a replacement for composer global require.
# This ensures that dependencies used by applications installed via composer do not conflict.
RUN mkdir --parents /opt/composer && \
  cd /opt/composer && \
  composer init --require=consolidation/cgr:^2 -n && \
  composer config bin-dir /usr/local/bin && \
  composer install
ENV CGR_BIN_DIR /usr/local/bin

# Install drush 8 via composer
RUN cgr drush/drush:8.*

# Install mailhog sender for mailhog integration
RUN \
  curl --location --output /usr/local/bin/mhsendmail https://github.com/mailhog/mhsendmail/releases/download/v0.2.0/mhsendmail_linux_amd64 && \
  chmod +x /usr/local/bin/mhsendmail

# Install wait-for-it application
# https://github.com/vishnubob/wait-for-it
ADD \
  https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it
RUN \
  chmod +x /usr/local/bin/wait-for-it

# Put our configurations in place, done as the last step to be able to override
# default settings from packages.
COPY files/etc/ /etc/

# Add our tools to PATH.
COPY files/bin /usr/local/bin/

RUN phpenmod drupal-recommended

ENV PHP_DEFAULT_EXTENSIONS calendar ctype curl dom exif fileinfo ftp gd gettext iconv json mysqli mysqlnd opcache pdo pdo_mysql pdo_sqlite phar posix readline shmop simplexml soap sockets sqlite sysvmsg sysvsem sysvshm tokenizer wddx xml xmlreader xmlwriter xsl mbstring zip

HEALTHCHECK --interval=5s CMD ["sh", "-c", "[ -e /tmp/docker-finished-init ]"]

EXPOSE 9000
