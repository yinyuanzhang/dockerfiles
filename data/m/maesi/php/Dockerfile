FROM php:7.1-apache-stretch

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd mysqli \
    && docker-php-ext-install pdo_mysql

# Override with custom opcache settings
COPY config.ini $PHP_INI_DIR/conf.d/
RUN chmod a+rwx -R /var/www/html
