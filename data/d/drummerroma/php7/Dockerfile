FROM php:7.2-fpm

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libpq-dev \
        g++ \
        libicu-dev \
        libxml2-dev \
        git \
        nano \
				libmagickwand-dev --no-install-recommends \
    && docker-php-ext-configure intl \
    && docker-php-ext-install mbstring \
    && docker-php-ext-install intl \
    && docker-php-ext-install zip \
    && docker-php-ext-install pdo_mysql \
    && docker-php-ext-install pdo_pgsql \
    && docker-php-ext-install soap \
    && docker-php-ext-install mysqli \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
		&& apt-get purge --auto-remove -y g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pecl install apcu \
		&& pecl install imagick \
		&& pecl install -o -f redis \
		&& pecl install xdebug \
    && docker-php-ext-enable apcu imagick redis xdebug \
    && pecl clear-cache

# new: run wordpress client
# https://github.com/wp-cli/wp-cli
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
RUN chmod +x wp-cli.phar \
    && mv wp-cli.phar /usr/local/bin/wp


RUN sed -i -e 's/listen.*/listen = 0.0.0.0:9000/' /usr/local/etc/php-fpm.conf

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# remove unnecessary files
RUN rm -rf /var/lib/apt/lists/*

RUN usermod -u 1000 www-data

WORKDIR /var/www

CMD ["php-fpm"]



