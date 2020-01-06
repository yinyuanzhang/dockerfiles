##
# PHP Image
##
FROM php:7.2.7-apache-stretch

# Allow port 80 binding
RUN apt-get update \
    && apt-get install -qy libcap2-bin \
    && setcap cap_net_bind_service=+ep /usr/sbin/apache2

# PHP extensions
# imagick, bcmath, gd, intl, pcntl, pdo_mysql, redis, zip
RUN apt-get update \
    && apt-get install -qy \
        libfreetype6 \
        libfreetype6-dev \
	    libicu57 \
        libicu-dev \
        imagemagick-6-common \
        libmagickcore-dev \
        libmagickwand-6.q16-3 \
        libmagickcore-6.q16-3-extra \
        libmagickwand-dev \
        libpq5 \
        libpq-dev\
        libjpeg62-turbo \
        libjpeg62-turbo-dev \
        libwebp6 \
        libwebp-dev \
    && pecl install imagick redis \
    && docker-php-ext-enable imagick redis \
    && docker-php-ext-configure gd \
        --with-freetype-dir=/usr/include/ \
	    --with-jpeg-dir=/usr/include/ \
	    --with-webp-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) \
        bcmath \
        gd \
        intl \
        pcntl \
        pdo_mysql \
        pdo_pgsql \
        zip \
    && apt-get remove -qy \
        libfreetype6-dev \
        libicu-dev \
        libmagickcore-dev \
        libmagickwand-dev \
        libpq-dev \
        libjpeg62-turbo-dev \
        libwebp-dev \
    && apt-get autoremove -qy \
    && rm -rf /var/lib/apt/lists/*

# Composer
RUN EXPECTED_COMPOSER_SIGNATURE=$(curl -sS https://composer.github.io/installer.sig) \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '${EXPECTED_COMPOSER_SIGNATURE}') { echo 'Composer.phar Installer verified'; } else { echo 'Composer.phar Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');"

# Runtime tools
RUN apt-get update \
    && apt-get install -qy \
        gettext \
        git \
        mysql-client \
        perl \
        redis-tools \
    && rm -rf /var/lib/apt/lists/*

ENV HOME /var/www
RUN usermod -u 1000 -d /var/www www-data \
    && groupmod -g 1000 www-data \
    && rm -rf /var/www \
    && mkdir -p /var/www/app \
    && chown www-data:www-data -R /var/www

COPY php.ini /usr/local/etc/php/
COPY vhost.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite \
    && chown www-data:www-data /var/run/apache2

USER www-data
WORKDIR /var/www/app
RUN composer global require hirak/prestissimo
