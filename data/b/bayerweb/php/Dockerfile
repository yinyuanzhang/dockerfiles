FROM php:7.1
MAINTAINER LABEL nirmal.arya@cognizant.com

# Set Environment variables (can be changed on docker run with -e)
ENV PATH="/root/.composer/vendor/bin:${PATH}"

# Install dependencies
RUN set -ex \
  && apt-get update -yqq \
  && apt-get install -f -yqq \
    git \
    unzip \
    wget \
    curl \
    libmcrypt-dev \
    libgd2-dev \
    libgd2-xpm-dev \
    libbz2-dev \
    libcurl4-openssl-dev \
    libmagickwand-dev \
    libmemcached-dev \
    zlib1g-dev \
    mysql-client \
    openssh-client \
    wkhtmltopdf \
    nano \



  # Install required PHP extensions.
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) bz2 gd pdo_mysql mcrypt curl mbstring opcache zip \
  && pecl install xdebug \
  && pecl install memcached-3.0.4 \
  && docker-php-ext-enable memcached \

  # Install composer
  && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \

  # Add composer dependencies
  && composer global require "hirak/prestissimo:^0.3" \

  # Remove unwanted packages.
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

COPY config/php.ini /usr/local/etc/php/
CMD ["php", "-a"]