FROM php:7.1-apache

ENV APACHE_DOCUMENT_ROOT /var/www/public

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf \
    && sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

RUN a2enmod rewrite

RUN apt-get update && apt-get install wget git zip libjpeg-dev libwebp-dev \
libpng-dev libjpeg62-turbo-dev libjpeg-turbo-progs libjpeg62-turbo cron nano mysql-client gnupg -y

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -

RUN apt-get install -y nodejs

RUN npm i -g npm

RUN npm install yarn imagemin -g

RUN docker-php-ext-install pdo_mysql mysqli \
    && docker-php-ext-configure gd --with-png-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN pecl install -o -f redis \
    &&  rm -rf /tmp/pear \
    &&  docker-php-ext-enable redis

RUN echo "upload_max_filesize = 64M\npost_max_size = 128M\nmax_input_vars = 5000" > \
    /usr/local/etc/php/conf.d/project.ini

RUN rm /var/www -rf

COPY . /var/www/

RUN chown -R www-data:www-data /var/www

USER www-data

WORKDIR /var/www/

RUN yarn install --production

RUN composer install --no-interaction --no-dev \
    && composer dump-autoload -o

RUN npm run production

USER root

EXPOSE 80