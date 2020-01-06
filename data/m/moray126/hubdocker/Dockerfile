FROM php:5.6-apache
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        cron \
    && docker-php-ext-install -j$(nproc) iconv \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && docker-php-ext-install mysql mysqli pdo_mysql \
    && mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini" \
    && update-rc.d cron defaults \
    && echo "* * * * * /usr/local/bin/php /var/www/html/phpcms/modules/remotedata/pi.php vegetables dailay > /dev/null 2>&1" > /var/spool/cron/crontabs/root \
    && crontab /var/spool/cron/crontabs/root \
    && /etc/init.d/cron start \
    && update-rc.d cron enable
    
