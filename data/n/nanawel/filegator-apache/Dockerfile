FROM node:12 as node

COPY . /tmp/build

RUN cd /tmp/build \
    && npm install \
    && npm run build

FROM php:7.2-apache

RUN curl --location --output /usr/local/bin/composer https://getcomposer.org/composer.phar
RUN chmod +x /usr/local/bin/composer

RUN apt-get update && apt-get install --no-install-recommends -y \
        wget \
        bzip2 \
        unzip \
        libzip-dev \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-install -j$(nproc) zip \
    && rm -rf /tmp/*

COPY . /var/www
COPY --from=node /tmp/build/dist /var/www/dist

RUN mkdir /var/www/vendor \
    && chown www-data: /var/www/vendor /var/www/composer.* \
    && su -l www-data -s /bin/sh -c "php /usr/local/bin/composer --working-dir=/var/www install --no-dev" \
    && su -l www-data -s /bin/sh -c "php /usr/local/bin/composer require league/flysystem-sftp"

RUN cp -f /var/www/configuration_sample.php /var/www/configuration.php \
    && mkdir -p /var/www/storage \
    && chown -R www-data: /var/www/storage /var/www/private /var/www/repository \
    && chmod -R ug+rwX /var/www/storage /var/www/private /var/www/repository \
    && rm -rf /var/www/html \
    && ln -sfT /var/www/dist /var/www/html

