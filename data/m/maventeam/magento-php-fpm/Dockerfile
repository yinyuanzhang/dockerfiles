FROM php:5.6-fpm-stretch

RUN apt-get update && apt-get install -y \
        bzip2\
        libicu57 \
        libexif12 \
        libjpeg62-turbo\
        libmcrypt4  \
        libpng16-16 \
        libxml2\
        libxslt1.1 \
        libfreetype6 \
        libpcre3 \
        curl \
        apt-transport-https \
        software-properties-common \
    && apt-get clean && apt-get --yes --quiet autoremove --purge \
    && rm -rf  /var/lib/apt/lists/* /tmp/* /var/tmp/* \
        /usr/share/doc/* /usr/share/groff/* /usr/share/info/* /usr/share/linda/* \
        /usr/share/lintian/* /usr/share/locale/* /usr/share/man/*

RUN apt-get update && apt-get install -y \
        libzip-dev  \
        libicu-dev  \
        libexif-dev\
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libssh2-1-dev \
        libtool \
        libxml2-dev \
        libxslt-dev \
        libpcre3-dev \
        libfreetype6-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-configure hash --with-mhash \
    && docker-php-ext-install -j$(nproc) exif mcrypt intl xsl gd zip pdo_mysql opcache soap bcmath json iconv mbstring pcntl \
    && apt-get purge -y \
        libzip-dev  \
        libicu-dev  \
        libexif-dev\
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libssh2-1-dev \
        libtool \
        libxml2-dev \
        libxslt-dev \
        libpcre3-dev \
        libfreetype6-dev \
    && apt-get clean && apt-get --yes --quiet autoremove --purge \
    && rm -rf  /var/lib/apt/lists/* /tmp/* /var/tmp/* \
        /usr/share/doc/* /usr/share/groff/* /usr/share/info/* /usr/share/linda/* \
        /usr/share/lintian/* /usr/share/locale/* /usr/share/man/*


# Memory Limit
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini

# Time Zone
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" > $PHP_INI_DIR/conf.d/date_timezone.ini

WORKDIR /var/www
