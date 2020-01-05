FROM php:7.3-fpm

MAINTAINER massalitine@gmail.com
ENV ACCEPT_EULA=Y
ENV XDEBUG="false"
RUN apt-get update \
    && apt-get install -y --force-yes --no-install-recommends \
       libmemcached-dev \
       libz-dev \
       libpq-dev \
       libjpeg-dev \
       libpng-dev \
       libfreetype6-dev \
       libssl-dev \
       libmcrypt-dev \
       libmagickwand-dev \
       libxml2-dev \
       libzip-dev \
       cron \
    && docker-php-ext-install \
       soap \
       pcntl \
       zip \
       mbstring \
       pdo \
       pdo_mysql \
       bcmath \
       iconv \
    && pecl install mcrypt-1.0.2 && \
       docker-php-ext-enable mcrypt \
    && pecl install imagick && \
       docker-php-ext-enable imagick \
    # Install the PHP gd library
    && docker-php-ext-configure gd \
        --enable-gd-native-ttf \
        --with-jpeg-dir=/usr/lib \
        --with-freetype-dir=/usr/include/freetype2 && \
    docker-php-ext-install gd \
  # Install the xdebug extension
    && pecl install xdebug-beta && docker-php-ext-enable xdebug \
    && pecl install memcached && docker-php-ext-enable memcached \
  # Microsoft SQL Server Prerequisites
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    locales \
    apt-transport-https \
    gnupg2 \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/9/prod.list \
        > /etc/apt/sources.list.d/mssql-release.list \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
    && apt-get update \
    && apt-get -y --no-install-recommends install \
        unixodbc-dev \
        msodbcsql17 \
    && pecl install sqlsrv-5.5.0preview pdo_sqlsrv-5.5.0preview \
    && docker-php-ext-enable sqlsrv pdo_sqlsrv \
    && pecl install -o -f redis \
    && rm -rf /tmp/pear \
    && docker-php-ext-enable redis \
    && echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen \
    && apt-get remove -y --purge gnupg2 apt-transport-https \
    && rm -f /etc/apt/sources.list.d/mssql-release.list \
    && apt-get clean -y \
    && rm -r /var/lib/apt/lists/*


# Laravel Schedule Cron Job:
RUN echo "* * * * * root /usr/local/bin/php /var/www/artisan schedule:run >> /dev/null 2>&1"  >> /etc/cron.d/laravel-scheduler
RUN chmod 0644 /etc/cron.d/laravel-scheduler
ADD ./laravel.ini /usr/local/etc/php/conf.d
WORKDIR /var/www
COPY ./docker-entrypoint.sh /usr/local/bin/
# Copy xdebug configration for remote debugging
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN ln -s /usr/local/bin/docker-entrypoint.sh /
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 9000
CMD ["php-fpm"]
