FROM php:5.6-fpm

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libjpeg-dev \
        libpng-dev \
        libgearman-dev \
        libicu-dev \
        libtidy-dev \
        python-dev libxml2-dev libxslt1-dev zlib1g-dev supervisor ssh \
        mc vim sudo \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd \
    && pecl install gearman \
    && docker-php-ext-install \
            intl \
            mysqli \
            pdo_mysql \
            soap \
            tidy \
            xsl \
            zip \
            exif \
    && docker-php-ext-enable gearman exif \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

COPY php.ini-production "$PHP_INI_DIR/php.ini"

EXPOSE 9000

#FROM php:5.6-fpm-alpine
#ARG TIMEZONE=Europe/Moscow
#
#COPY php.ini-production "$PHP_INI_DIR/php.ini"
#
#RUN apk add --update \
#    openssl unzip curl libmemcached zlib libmcrypt gnupg jpegoptim icu-dev \
#    freetype libpng libjpeg-turbo freetype-dev libpng-dev libjpeg-turbo-dev \
#    python python-dev py-pip supervisor \
#    && pip install gearman \
#    && docker-php-ext-install pdo_mysql intl mysqli soap tidy xsl zip \
#    && docker-php-ext-enable pdo_mysql gearman \
#    && docker-php-ext-configure gd \
#        --with-gd \
#        --with-freetype-dir=/usr/include/ \
#        --with-png-dir=/usr/include/ \
#        --with-jpeg-dir=/usr/include/ \
#    && NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \
#    && docker-php-ext-install -j${NPROC} gd \
#    && apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev \
#    && ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \
#    && echo ${TIMEZONE} > /etc/timezone \
#    && printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} > /usr/local/etc/php/conf.d/tzone.ini \
#    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
#
#EXPOSE 9000