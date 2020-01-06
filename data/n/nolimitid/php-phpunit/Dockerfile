# NolimitID docker images with php5, composer,
# and phpunit.

FROM ubuntu:14.04.3

MAINTAINER maman <achmad@mahardi.me>

# Commands
RUN \
  apt-get update && \
  apt-get upgrade -y --force-yes && \
  apt-get install -y --force-yes git wget curl ca-certificates bzip2 rsync \
  ssh php5-cli php5-dev php-pear php5-mysql php5-pgsql php5-sqlite php5-apcu \
  php5-json php5-curl php5-dev php5-gd php5-gmp php5-imap php5-mcrypt \
  php5-xdebug php5-memcached && \

  # enable mcrypt
  # ln -s /etc/php5/conf.d/mcrypt.ini /etc/php5/mods-available && \
  php5enmod mcrypt && \

  # install composer
  curl -sS https://getcomposer.org/installer | php && \
  mv composer.phar /usr/bin/composer && \

  # install phpunit
  mkdir -p /srv/var && \
  wget -q --no-check-certificate -O /tmp/phpunit.phar https://phar.phpunit.de/phpunit.phar && \
  chmod +x /tmp/phpunit.phar && \
  mv /tmp/phpunit.phar /srv/var/phpunit && \
  ln -s /srv/var/phpunit /usr/bin/phpunit && \

  # housekeeping
  apt-get autoremove -y && \
  apt-get clean all

