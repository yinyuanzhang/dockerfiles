FROM phalconphp/php-fpm:7.1-min
WORKDIR /var/www

RUN mkdir -p /var/cache/apt/archives/partial && mkdir -p /var/log/apt

RUN apt-get update && \
  apt-get install -y --no-install-recommends apt-utils && \
  apt-get install -y nano zip unzip php-pclzip git pkg-config libssl-dev libsasl2-dev

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php && \
  mv composer.phar /usr/local/bin/composer

# Cleanup package manager
RUN apt-get autoremove -y && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
