FROM php:7.2-apache

# install the PHP extensions we need
RUN apt-get update && apt-get install -y libpng-dev \
  libjpeg-dev \
  libpq-dev \
  libicu-dev \ 
  libfreetype6-dev \
  libmcrypt-dev \
  && rm -rf /var/lib/apt/lists/*

# clean after install
RUN apt-get clean

# install php extension
RUN /usr/local/bin/docker-php-ext-install -j$(nproc) \
  intl \
  pcntl \
  gd \
  mbstring \
  pdo \
  pdo_mysql \
  pdo_pgsql \
  zip \
  mysqli

RUN pecl install mcrypt-1.0.2 \
  && docker-php-ext-enable mcrypt

# configure php extension
RUN /usr/local/bin/docker-php-ext-configure \
  gd --with-png-dir=/usr/include/ \
  --with-jpeg-dir=/usr/include/ \
  --with-freetype-dir=/usr/include/

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && php -r "if (hash_file('sha384', 'composer-setup.php') === '48e3236262b34d30969dca3c37281b3b4bbe3221bda826ac6a9a62d6444cdb0dcd0615698a5cbe587c3f0fe57a54d8f5') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
  && php composer-setup.php \
  && php -r "unlink('composer-setup.php');"


RUN mv composer.phar /bin/composer

RUN adduser --disabled-password --gecos "" composer \
  && mkdir -p /home/composer/.composer \
  && chown -R composer:composer /home/composer/.composer \
  && ls /home/composer/.composer

COPY ./run_composer.sh /home/composer/run_composer.sh

RUN echo 'alias composer="/bin/sh /home/composer/run_composer.sh"' >> /root/.bashrc
RUN a2enmod rewrite

WORKDIR /var/www/html
