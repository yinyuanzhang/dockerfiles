FROM php:7.2.1-fpm

RUN apt-get update && apt-get install -y ssh libmcrypt-dev \
    mysql-client libmagickwand-dev wget sudo --no-install-recommends \
    && pecl install imagick \
    && docker-php-ext-enable imagick \
    && docker-php-ext-install pdo_mysql exif mbstring zip  \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  \
    && docker-php-ext-install gd \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb \
    ;sudo apt-get install -f -y

RUN composer require --dev laravel/dusk \
    && chmod 775 vendor/laravel/dusk/bin/*

CMD ["vendor/laravel/dusk/bin/chromedriver-linux"]

EXPOSE 9515
