FROM php:7.3-fpm-stretch

COPY forego.deb /tmp/

RUN apt install /tmp/forego.deb
RUN apt-get update && apt-get install -y \
    # Git
    git-core \
    # GD
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    # Curl
    libssl-dev \
    libcurl4-openssl-dev \
    # xml
    libxml2-dev \
    # libzip
    libzip-dev \
    # bzip2
    libbz2-dev \
    # GMP
    libgmp3-dev \
    # intl
    libicu-dev \
    # memcached
    libmemcached-dev \
    # imagick
    libmagickwand-dev \
    libmagickcore-dev \
    # mysql command line tool
    default-mysql-client \
    # jpegtran
    libjpeg-turbo-progs \
  && docker-php-ext-install -j$(nproc) \
    mysqli pdo pdo_mysql \
    gmp bcmath \
    zip bz2 \
    mbstring \
    exif \
    curl \
    intl \
    xml \
  && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
  && docker-php-ext-install -j$(nproc) gd \
  \
  && for i in $(seq 1 3); do pecl install -o igbinary && s=0 && break || s=$? && sleep 1; done; (exit $s) \
  && docker-php-ext-enable igbinary \
  \
  && for i in $(seq 1 3); do echo no | pecl install -o --nobuild memcached && s=0 && break || s=$? && sleep 1; done; (exit $s) \
  && cd "$(pecl config-get temp_dir)/memcached" \
  && phpize \
  && ./configure --enable-memcached-igbinary \
  && make \
  && make install \
  && docker-php-ext-enable memcached \
  && cd - \
  \
  && pecl install \
    imagick \
  && docker-php-ext-enable \
    imagick \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
