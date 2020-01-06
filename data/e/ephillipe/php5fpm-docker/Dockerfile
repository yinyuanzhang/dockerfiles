FROM php:5-fpm
# Install modules
RUN apt-get update && apt-get install -y \
        zlib1g-dev \
        php5-pgsql \
        libpq-dev \
        locales-all \
        postgresql-client \
        libghc-postgresql-libpq-dev \
    && docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql/ \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install zip pgsql pdo_pgsql gd
CMD ["php-fpm"]
