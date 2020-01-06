FROM php:alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# Install dev dependencies
RUN  apk add --no-cache --virtual .build-deps \
  $PHPIZE_DEPS \
  curl-dev \
  imagemagick-dev \
  libtool \
  libxml2-dev \
  postgresql-dev \
  sqlite-dev

# Install production dependencies
RUN apk add --no-cache \
  bash \
  curl \
  g++ \
  gcc \
  git \
  imagemagick \
  libc-dev \
  libpng-dev \
  make \
  mysql-client \
  nodejs \
  nodejs-npm \
  yarn \
  openssh-client \
  postgresql-libs \
  rsync \
  zlib-dev \
  libzip-dev

# Install PECL and PEAR extensions
RUN pecl install \
  imagick

# Install and enable php extensions
RUN docker-php-ext-enable \
  imagick
RUN docker-php-ext-configure zip --with-libzip
RUN docker-php-ext-install \
  curl \
  iconv \
  mbstring \
  pdo \
  pdo_mysql \
  pdo_pgsql \
  pdo_sqlite \
  pcntl \
  tokenizer \
  xml \
  gd \
  zip \
  bcmath

# Install composer
ENV COMPOSER_HOME /composer
ENV PATH ./vendor/bin:/composer/vendor/bin:$PATH
ENV COMPOSER_ALLOW_SUPERUSER 1
RUN curl -s https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin/ --filename=composer

# use chinese mirrors
RUN composer config -g repo.packagist composer https://mirrors.aliyun.com/composer/
# Install PHP_CodeSniffer
RUN composer global require "squizlabs/php_codesniffer=*"
# Install Envoy
RUN composer global require "laravel/envoy=~1.0"

RUN curl -LO https://deployer.org/deployer.phar && \
  mv deployer.phar /usr/local/bin/dep && \
  chmod +x /usr/local/bin/dep 

# Cleanup dev dependencies
RUN apk del -f .build-deps

# Setup working directory
WORKDIR /var/www