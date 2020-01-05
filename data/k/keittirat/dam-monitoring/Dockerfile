# --- Prepare PHP Package
FROM composer as PHPVendor
WORKDIR /package
COPY composer.* ./
RUN composer install  \
    --ignore-platform-reqs \
    --no-interaction \
    --no-plugins \
    --no-scripts \
    --prefer-dist \
    --no-autoloader

# --- Build frontend assets
FROM node:10 as Frontend
WORKDIR /build

RUN curl https://getcomposer.org/composer.phar -o composer.phar \
    && chmod +x composer.phar

COPY .babelrc webpack.mix.js ./
COPY package*.json ./
# RUN npm ci
RUN npm install

COPY public /build/public
COPY artisan /build/artisan
COPY resources /build/resources
RUN npm run prod

# --- Combined all builed files
FROM php:7.2-fpm-alpine
WORKDIR /var/www/html/dam-monitoring

ARG COMMIT_HASH
ARG BUILD_TAG

RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"

COPY app ./app
COPY bootstrap ./bootstrap
COPY config ./config
COPY database ./database
COPY routes ./routes
COPY storage ./storage

COPY .env.example .env
COPY server.php artisan composer.* ./

# Add Version and Tag
RUN echo "COMMIT_HASH=${COMMIT_HASH}" >> .env \
    && echo "BUILD_TAG=${BUILD_TAG}" >> .env

COPY resources/views ./resources/views
COPY --from=PHPVendor /package/vendor ./vendor
COPY --from=Frontend /build/composer.phar ./composer.phar
COPY --from=Frontend /build/public ./public

# Build PHP + Build autoload
RUN php composer.phar dumpautoload \
    && php artisan key:generate

# Remove unnecessary file
RUN rm -rf composer.phar

VOLUME /var/www/html
