# FROM node:stretch
FROM php:7.3.2-fpm-stretch AS ext-mongodb

ENV EXT_MONGODB_VERSION=1.5.2

RUN docker-php-source extract \
    && apt-get update && apt-get install git -y \
    && git clone --branch $EXT_MONGODB_VERSION --depth 1 https://github.com/mongodb/mongo-php-driver.git /usr/src/php/ext/mongodb \
    && cd /usr/src/php/ext/mongodb && git submodule update --init \
    && docker-php-ext-install mongodb

FROM php:7.3.2-fpm-stretch

# ext-mongodb
COPY --from=ext-mongodb /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini
COPY --from=ext-mongodb /usr/local/lib/php/extensions/no-debug-non-zts-20180731/mongodb.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/mongodb.so


# Copy composer and package json
COPY composer.lock composer.json /var/www/
COPY package*.json /var/www/

# Set working directory
WORKDIR /var/www
# Alpine Update and Upgrade
RUN apt-get update

# Install dependencies
RUN apt-get install -y \
    build-essential \
    libpng-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    locales \
    zip \
    jpegoptim optipng pngquant gifsicle \
    vim \
    unzip \
    git \
    curl

# Installing postgre full
RUN apt-get install -y libpq-dev
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql
RUN docker-php-ext-install pdo pdo_pgsql

# Installing gd
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ --with-png-dir=/usr/include/
RUN docker-php-ext-install gd

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install node and npm by apt-get
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs \
    npm

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Add user for laravel application
RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

# Copy existing application directory contents
COPY . /var/www

# Copy existing application directory permissions
COPY --chown=www:www . /var/www

# Change current user to www
USER www

# Expose port 9000 and start php-fpm server
EXPOSE 9000
CMD ["php-fpm"]
# ENTRYPOINT ["build-essential", "libpng-dev", "libjpeg62-turbo-dev", "libfreetype6-dev", "locales", "zip", "jpegoptim optipng pngquant gifsicle", "vim", "unzip", "git", "curl", "postgresql", "postgresql-dev"]
