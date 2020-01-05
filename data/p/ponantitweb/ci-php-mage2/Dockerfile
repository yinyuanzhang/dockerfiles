FROM php:7.1.23

RUN apt-get update && apt-get install -y \
    libmcrypt-dev \
    libxslt-dev \
    libfreetype6-dev libjpeg62-turbo-dev libpng-dev mysql-client procps locales \
    unzip \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && docker-php-ext-install xsl pdo_mysql bcmath intl soap zip \
    && docker-php-ext-install -j$(nproc) mcrypt \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd
    # && mv "$PHP_INI_DIR/php.ini-development" "$PHP_INI_DIR/php.ini"
COPY php.ini "$PHP_INI_DIR/php.ini"
RUN echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen \ 
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "it_IT.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "en_AU.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "fr_BE.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "fr_CH.UTF-8 UTF-8" >> /etc/locale.gen \
    && echo "en_HK.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen
