FROM php:7.1
ENV DEBIAN_FRONTEND="noninteractive"
RUN echo 'deb http://ftp.debian.org/debian stretch-backports main' > /etc/apt/sources.list.d/stretch-backports.list
RUN apt-get update -yqq && apt-get upgrade -yqq
RUN apt-get install -yqq --no-install-recommends -t stretch-backports librdkafka-dev
RUN apt-get install wget unzip gzip zlib1g-dev -yqq
RUN docker-php-ext-install zip pdo_mysql
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/76a7060ccb93902cd7576b67264ad91c8a2700e2/web/installer -O - -q | php -- --quiet && mv composer.phar /usr/local/bin/composer
RUN pecl update-channels && pecl install rdkafka-3.0.4 apcu xdebug && docker-php-ext-enable rdkafka apcu xdebug
