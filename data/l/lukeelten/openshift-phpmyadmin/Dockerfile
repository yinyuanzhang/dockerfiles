FROM php:apache

LABEL author="Tobias Derksen <tobias.derksen@codecentric.de>"
ARG PMA_VERSION="STABLE"

RUN mkdir -p /tmp/pma && chmod -R 777 /tmp/pma

RUN apt-get update && \
    apt-get -y install git unzip zip libzip-dev && \
    docker-php-ext-install mysqli zip && \
    apt-get clean
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php composer-setup.php && \
    rm -f composer-setup.php && \
    mv composer.phar /usr/local/bin/composer

RUN git clone -b "${PMA_VERSION}" --depth 1 https://github.com/phpmyadmin/phpmyadmin.git . && \
    composer install --no-dev -o -n

COPY config.inc.php .
COPY apache2.conf /etc/apache2/apache2.conf

