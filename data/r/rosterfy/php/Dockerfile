FROM php:7.1.8-fpm

RUN curl -sL https://deb.nodesource.com/setup_11.x  | bash - \
    && apt-get update \
    && yes | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \
    && apt-get install -y nginx netcat git supervisor libmcrypt-dev libicu-dev mysql-client nodejs libmagickwand-dev --no-install-recommends \
    && docker-php-ext-install -j$(nproc) mcrypt pdo_mysql intl gd zip \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && rm /etc/nginx/sites-enabled/default

COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

RUN composer global require "squizlabs/php_codesniffer=*" \
    && ln -s /root/.composer/vendor/bin/phpcs /usr/local/bin/phpcs

RUN composer global require "phpunit/phpunit:~5.3.4" --prefer-source --no-interaction \
    && ln -s /root/.composer/vendor/bin/phpunit /usr/local/bin/phpunit

RUN groupadd -g 1000 hostuser
RUN useradd -m -g 1000 -u 1000 hostuser
