FROM php:7.2.5-apache
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
        libicu-dev \
        libmemcached-dev \
        libbz2-dev \
        git \
    && a2enmod rewrite \
    && docker-php-ext-install bcmath bz2 calendar exif opcache pdo_mysql intl zip \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd \
    && pecl install memcached \
    && docker-php-ext-enable memcached
RUN pecl install https://xdebug.org/files/xdebug-2.6.0.tgz \
    && docker-php-ext-enable xdebug \
    && echo "error_reporting = E_ALL" > /usr/local/etc/php/php.ini \
    && echo "display_startup_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "display_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "expose_php = Off" >> /usr/local/etc/php/php.ini \
    && echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN bash -c 'echo -e "Listen 81\n" >> /etc/apache2/ports.conf' \
    && bash -c 'echo -e "\n<VirtualHost *:81>\n\tServerAdmin webmaster@localhost\n\tDocumentRoot /var/www/backend/web\n\tErrorLog \${APACHE_LOG_DIR}/error-backend.log\n\tCustomLog \${APACHE_LOG_DIR}/access-backend.log combined\n</VirtualHost>\n" >> /etc/apache2/sites-available/000-default.conf' \
    && mkdir -p /var/www/backend/web
RUN sed -i 's/\/var\/www\/html/\/var\/www\/frontend\/web/g' /etc/apache2/sites-available/000-default.conf \
    && mkdir -p /var/www/frontend \
    && mv /var/www/html /var/www/frontend/web
