FROM php:7.3.13-fpm

RUN apt-get update && apt-get install -y libpq-dev \
                            libzip-dev zip \
                            # Required for CircleCI to install ORBs
                            gnupg \
                            # Required by many tools to decode JSON in command line
                            jq \
    # Install PDO PostgreSQL
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-enable pdo_pgsql \
    # Install zip
    && docker-php-ext-configure zip --with-libzip \
    && docker-php-ext-install zip \
    # Install pcntl (required by Laravel Horizon)
    && docker-php-ext-install pcntl \
    # Install bcmath (required by Laravel Telescope)
    && docker-php-ext-install bcmath \
    # Install OPcache
    && docker-php-ext-install opcache \
    # Install redis
    && pecl install --onlyreqdeps redis \
    && docker-php-ext-enable redis \
    # Cleanup
    && apt-get -y autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

COPY /php/conf.d/opcache.ini /usr/local/etc/php/conf.d/opcache.ini
COPY /php-fpm.d/zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf

COPY --from=composer:1.9.1 /usr/bin/composer /usr/bin/composer
