FROM php:7.3-fpm

LABEL maintainer="Inventis <developers@inventis.be>"

# Install gd, iconv libs
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libzip-dev \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

# Install mcrypt if available
RUN (apt-get install -y --ignore-missing libmcrypt-dev mcrypt \
    && docker-php-ext-install -j$(nproc) mcrypt) || true

# Install PHP extensions
RUN apt-get update && apt-get install -y \
      libicu-dev \
      libxml2-dev \
    && rm -r /var/lib/apt/lists/* \
    && docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \
    && docker-php-ext-install -j$(nproc) \
      exif \
      intl \
      mbstring \
      pcntl \
      pdo_mysql \
      soap \
      zip \
      opcache
RUN (pecl install apcu \
    && echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini) || true

# Configure PHP default behaviour
COPY php-ini-overrides.ini /usr/local/etc/php/conf.d/php-ini-overrides.ini
COPY php-fpm-ini-overrides.ini /usr/local/etc/php/conf.d/php-fpm-ini-overrides.ini

# Install Xdebug
RUN curl -fsSL 'https://xdebug.org/files/xdebug-2.7.0beta1.tgz' -o xdebug.tar.gz \
    && mkdir -p xdebug \
    && tar -xf xdebug.tar.gz -C xdebug --strip-components=1 \
    && rm xdebug.tar.gz \
    && ( \
    cd xdebug \
    && phpize \
    && ./configure --enable-xdebug \
    && make -j$(nproc) \
    && make install \
    ) \
    && rm -r xdebug \
    && docker-php-ext-enable xdebug

COPY xdebug-config.ini /usr/local/etc/php/conf.d/xdebug-config.ini

# Enable appropriate locales
RUN apt-get update && apt-get install -y \
    locales

RUN echo 'de_DE ISO-8859-1\n \
    de_DE.UTF-8 UTF-8\n \
    de_DE@euro ISO-8859-15\n \
    en_GB ISO-8859-1\n \
    en_GB.ISO-8859-15 ISO-8859-15\n \
    en_US ISO-8859-1\n \
    en_US.ISO-8859-15 ISO-8859-15\n \
    en_US.UTF-8 UTF-8\n \
    fr_FR ISO-8859-1\n \
    fr_FR.UTF-8 UTF-8\n \
    fr_FR@euro ISO-8859-15\n \
    nl_BE ISO-8859-1\n \
    nl_BE.UTF-8 UTF-8\n \
    nl_BE@euro ISO-8859-15\n \
    nl_NL ISO-8859-1\n \
    nl_NL.UTF-8 UTF-8\n \
    nl_NL@euro ISO-8859-15\n' \
    >> /etc/locale.gen &&  \
    /usr/sbin/locale-gen

# Update timezone
RUN echo 'Europe/Brussels' > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

COPY docker-entrypoint /usr/local/bin/
COPY plugins.sh /
ENTRYPOINT ["docker-entrypoint"]
CMD ["php-fpm"]
