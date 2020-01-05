FROM php:7.3-apache

RUN mv /var/www/html /var/www/web \
    && sed -ri "s%/var/www/html%/var/www/web%g" /etc/apache2/sites-available/* /etc/apache2/apache2.conf \
    && sed -i '/^#AddDefaultCharset.*$/a AddType text/html;charset=utf-8 html' /etc/apache2/conf-enabled/charset.conf \
    && sed -i '/^#AddDefaultCharset.*$/a AddCharset UTF-8 html' /etc/apache2/conf-enabled/charset.conf \
    && echo "umask 002" > /etc/apache2/conf-available/envvars

# Enable Apache Rewrite Module
RUN a2enmod rewrite expires

RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \
	libc-client-dev libicu-dev libmcrypt-dev libssl-dev libpng-dev libjpeg-dev \
    libxml2-dev libzip-dev unzip zip gzip less \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \
    docker-php-ext-install -j$(nproc)   \
        intl mbstring mysqli pdo pdo_mysql           \
        gd opcache soap zip phar

RUN { \
        echo 'date.timezone = "Europe/Berlin"';     \
	echo 'zlib.output_compression = On';        \
	echo 'zlib.output_compression_level = 6';   \
        echo 'memory_limit = 1024M';                \
        echo 'max_execution_time = 90';            \
        echo 'upload_max_filesize = 30M';           \
        echo 'post_max_size = 32M';                 \
        echo 'log_errors = On';                     \
        echo 'error_log = "/var/www/php.log"';      \
    } > $PHP_INI_DIR/conf.d/wordpress.ini

# set recommended PHP.ini settings
# see https://secure.php.net/manual/en/opcache.installation.php
RUN { \
        echo 'opcache.memory_consumption=128'; \
        echo 'opcache.interned_strings_buffer=8'; \
        echo 'opcache.max_accelerated_files=4000'; \
        echo 'opcache.revalidate_freq=60'; \
        echo 'opcache.fast_shutdown=1'; \
        echo 'opcache.enable_cli=0'; \
    } > $PHP_INI_DIR/conf.d/opcache-recommended.ini

WORKDIR /var/www

CMD ["apache2-foreground"]
