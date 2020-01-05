FROM php:7.0-fpm

# Installing first the libraries necessary to configure and install gd
RUN apt-get update && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev unzip cron mysql-client zip libxslt1-dev libmcrypt-dev libicu-dev gzip lsof libpng-dev
# Now we can configure and install the extension
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install bcmath intl mbstring mcrypt opcache pdo_mysql soap xsl zip

RUN groupadd -g 1000 app \
 && useradd -g 1000 -u 1000 -d /var/www -s /bin/bash app

COPY conf/www.conf /usr/local/etc/php-fpm.d/
COPY conf/php.ini /usr/local/etc/php/
COPY conf/php-fpm.conf /usr/local/etc/

RUN mkdir /sock
RUN chown -R app:app /usr/local/etc/php/conf.d /sock

USER app:app

WORKDIR /var/www/html