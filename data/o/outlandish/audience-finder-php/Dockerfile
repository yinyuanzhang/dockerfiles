FROM php:7.1-fpm

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug \
    && echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_enable_trigger=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.profiler_output_dir=/app/profiling" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

RUN echo "date.timezone=Europe/London" > /usr/local/etc/php/conf.d/zz-custom.ini \
    && echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/zz-custom.ini \
    && echo "display_errors = on" >> /usr/local/etc/php/conf.d/zz-custom.ini \
    && echo "session.autostart=0" >> /usr/local/etc/php/conf.d/zz-custom.ini

ENV PATH "$PATH:/var/www/html/vendor/bin"

RUN echo "env[\"XDEBUG_CONFIG\"] = \$XDEBUG_CONFIG" >> /usr/local/etc/php-fpm.d/zz-docker.conf

RUN docker-php-ext-install mysqli pdo pdo_mysql mbstring

RUN apt-get update && apt-get install -y \
        libicu-dev \
    && docker-php-ext-install intl \
    && apt-get remove -y \
        libicu-dev \
    && apt-get install -y \
        libicu57

RUN apt-get update && apt-get install libcurl4-openssl-dev -y \
    && docker-php-ext-install curl \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false libcurl4-openssl-dev -y

RUN apt-get install libxml2-dev -y \
    && docker-php-ext-install xml \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false libxml2-dev -y

RUN apt-get update && apt-get install -y \
        zlib1g-dev \
    && docker-php-ext-install zip \
    && apt-get remove -y \
        zlib1g-dev \
    && apt-get install -y \
        zlib1g

RUN apt-get update && apt-get install -y \
        libmcrypt-dev \
    && docker-php-ext-install mcrypt \
    && apt-get remove -y \
        libmcrypt-dev \
    && apt-get install -y \
        libmcrypt4

RUN apt-get update && apt-get install -y --no-install-recommends libmagickwand-dev \
    && pecl install imagick-3.4.3 \
    && docker-php-ext-enable imagick

RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends unzip libssl-dev libpcre3 libpcre3-dev \
    && cd /tmp \
    && curl -sSL -o php7.zip https://github.com/websupport-sk/pecl-memcache/archive/php7.zip \
    && unzip php7 \
    && cd pecl-memcache-php7 \
    && /usr/local/bin/phpize \
    && ./configure --with-php-config=/usr/local/bin/php-config \
    && make \
    && make install \
    && echo "extension=memcache.so" > /usr/local/etc/php/conf.d/ext-memcache.ini \
    && rm -rf /tmp/pecl-memcache-php7 php7.zip
    
RUN docker-php-ext-configure opcache --enable-opcache \
    && docker-php-ext-install opcache

RUN apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
    
COPY --from=composer /usr/bin/composer /usr/bin/composer

