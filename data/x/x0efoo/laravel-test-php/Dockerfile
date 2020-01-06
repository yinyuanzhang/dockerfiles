FROM php:7.3-fpm-alpine

WORKDIR /srv/app

RUN apk add --no-cache --update --virtual \
    buildDeps \
    autoconf \
    openssl-dev \
    g++ \
    make

RUN pecl install \
    redis

RUN docker-php-ext-install \
    pdo \
    pdo_mysql

RUN docker-php-ext-enable \
    redis

RUN apk del \
    buildDeps \
    autoconf \
    openssl-dev \
    g++ \
    make

# Install composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/local/bin/ --filename=composer \
    php -r "unlink('composer-setup.php');"

COPY ./ /srv/app

RUN composer install --no-dev --no-interaction --no-progress --no-suggest --optimize-autoloader

RUN php artisan view:cache

RUN chown -R www-data:www-data /srv/app/storage
