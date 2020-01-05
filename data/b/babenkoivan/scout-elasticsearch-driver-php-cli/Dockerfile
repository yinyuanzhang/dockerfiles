ARG PHP_VERSION
FROM php:${PHP_VERSION}-cli-alpine

WORKDIR /app

# Install php extensions
RUN docker-php-ext-install bcmath pdo_mysql

# Install composer
RUN wget https://getcomposer.org/installer && \
    php installer --install-dir=/usr/local/bin/ --filename=composer && \
    rm installer && \
    composer global require --no-interaction --prefer-dist --update-no-dev hirak/prestissimo

# Copy shell scripts
COPY bin /usr/local/bin/
RUN chmod -R +x /usr/local/bin/

# Install Laravel
ARG LARAVEL_VERSION
RUN composer create-project --no-interaction --prefer-dist laravel/laravel . $LARAVEL_VERSION

# Copy app files
RUN rm -rf database && mkdir -p database/factories
COPY database database
COPY app app

# Install Scout Elasticsearch Driver
RUN composer require --no-interaction --prefer-dist babenkoivan/scout-elasticsearch-driver

# Publish configs
RUN php artisan vendor:publish --provider="Laravel\Scout\ScoutServiceProvider" && \
    php artisan vendor:publish --provider="ScoutElastic\ScoutElasticServiceProvider"
