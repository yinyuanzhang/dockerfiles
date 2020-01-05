FROM php:7.1-fpm
RUN apt-get update && \
    apt-get install -y mysql-client libjpeg62-turbo-dev libpng-dev libpq-dev unzip git imagemagick && \
    docker-php-ext-configure gd --with-jpeg-dir=/usr --with-png-dir=/usr && \
    docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql mysqli zip && \
    curl -sS https://getcomposer.org/installer | php && \
    chmod +x composer.phar && \
    mv composer.phar /usr/local/bin/composer && \
    /usr/local/bin/composer global require drush/drush:8.1.2 && \
    ln -s /root/.composer/vendor/drush/drush/drush /usr/local/bin/drush && \
    mkdir /app/ && \
    chmod -R 777 /tmp/
WORKDIR /app/

COPY ./etc/ /etc/
COPY ./var/ /var/
