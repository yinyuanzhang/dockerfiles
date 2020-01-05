FROM php:7.3.6-fpm-stretch

# install the PHP extensions we need
RUN apt-get update \
    && apt-get install -y --no-install-recommends libjpeg62-turbo-dev libzip-dev libgmp-dev libpng-dev libpq-dev libxrender1 libxext6 libfontconfig1 mysql-client cron wget \
    && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && mv wkhtmltox/bin/wkhtmlto* /usr/local/bin/ \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd \
        --with-jpeg-dir=/usr \
        --with-png-dir=/usr \
    && docker-php-ext-install -j "$(nproc)" gmp gd mbstring opcache pdo pdo_mysql pdo_pgsql zip \
    && apt-mark manual \
        libjpeg62-turbo \
        libpq5 \
    && yes | pecl install xdebug \
    && echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini.off

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
        echo 'opcache.memory_consumption=128'; \
        echo 'opcache.interned_strings_buffer=8'; \
        echo 'opcache.max_accelerated_files=4000'; \
        echo 'opcache.revalidate_freq=60'; \
        echo 'opcache.fast_shutdown=1'; \
        echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

