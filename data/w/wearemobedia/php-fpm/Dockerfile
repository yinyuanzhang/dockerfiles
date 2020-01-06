FROM php:7.3.11-fpm-stretch

# install the PHP extensions we need
RUN apt-get update \
    && apt-get install -y --no-install-recommends libjpeg62-turbo-dev libpng-dev libpq-dev mysql-client wkhtmltopdf libzip-dev ghostscript libmagickwand-dev \
    && rm -rf /var/lib/apt/lists/* \
    && docker-php-ext-configure gd \
        --with-jpeg-dir=/usr \
        --with-png-dir=/usr \
    && docker-php-ext-install -j "$(nproc)" gd mbstring opcache pdo pdo_mysql pdo_pgsql zip \
    && apt-mark manual \
        libjpeg62-turbo \
        libpq5 \
    && yes | pecl install xdebug imagick \
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

# set upload size to 10M
RUN { \
        echo 'upload_max_filesize = 10M'; \
        echo 'post_max_size = 10M'; \
    } > /usr/local/etc/php/conf.d/upload-size.ini

RUN echo 'extension=imagick.so' > /usr/local/etc/php/conf.d/imagick.ini

