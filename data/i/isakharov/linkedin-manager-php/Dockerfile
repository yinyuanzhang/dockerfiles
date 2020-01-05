FROM php:7.2-fpm

# Needed for docker building on Ubuntu (keyboard layout auto config)
# Installation of wkhtmlto*
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y keyboard-configuration build-essential xorg libssl-dev libxrender-dev wget gdebi git
#    && wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb \
#    && dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb \
#    && apt-get install

# Installation of PHP extensions
RUN apt-get install -y zlib1g-dev libicu-dev g++ \
    && docker-php-ext-install pdo_mysql \
    && pecl install apcu-5.1.8 \
    && docker-php-ext-enable apcu \
    && docker-php-ext-configure intl \
    && docker-php-ext-install intl \
    && docker-php-ext-install zip

# Composer installation
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --filename=composer \
    && php -r "unlink('composer-setup.php');" \
    && mv composer /usr/local/bin/composer

WORKDIR /usr/src/app

RUN PATH=$PATH:/usr/src/apps/vendor/bin:bin
