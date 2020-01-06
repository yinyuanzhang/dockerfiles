FROM circleci/php:7.2-browsers

RUN sudo -E apt-get update && \
    sudo -E apt-get install -y libmagickwand-dev --no-install-recommends && \
    sudo -E pecl install imagick <<'' && \
    sudo -E docker-php-ext-enable imagick

RUN sudo -E apt-get update && \
    sudo -E apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev && \
    sudo -E docker-php-ext-install bcmath && \
    sudo -E docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    sudo -E docker-php-ext-install gd

RUN sudo -E docker-php-ext-install pdo_mysql mysqli && \
    sudo -E docker-php-ext-enable pdo_mysql mysqli
