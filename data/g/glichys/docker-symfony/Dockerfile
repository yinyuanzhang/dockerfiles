FROM ubuntu:16.04

RUN apt-get update -q \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -q -y git debconf-utils curl wget unzip \
    && apt-get install -q -y php php-mysql php-redis mysql-server redis-server php-gd php-intl php-curl php-mbstring php-xml php-zip \
    && curl -sS https://getcomposer.org/installer | php \
    && mv composer.phar /usr/local/bin/composer \
    && wget https://phar.phpunit.de/phpunit.phar \
    && chmod +x phpunit.phar \
    && mv phpunit.phar /usr/local/bin/phpunit
