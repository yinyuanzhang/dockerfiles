FROM php:7.1-apache-stretch

RUN apt-get -qq update \
    && apt-get -qq install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        libmemcached11 libmemcachedutil2 \
        build-essential libmemcached-dev \
        libz-dev git gnupg \
	libmagickwand-dev > /dev/null \
    && git clone --depth 1 -b master https://github.com/php-memcached-dev/php-memcached > /dev/null \
    && cd php-memcached \
    && phpize > /dev/null \
    && ./configure > /dev/null \
    && make > /dev/null \
    && make install > /dev/null \
    && cd .. \
    && echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcache.ini \
    && pecl install imagick-3.4.3 > /dev/null \
    && docker-php-ext-enable imagick > /dev/null \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ > /dev/null \
    && docker-php-ext-install gd mbstring mcrypt iconv mcrypt mysqli pdo_mysql opcache > /dev/null \
    && a2enmod rewrite \
    && a2enmod headers \
    && usermod -u 1000 www-data \
    && usermod -G staff www-data

RUN cd /tmp \
    && curl -s -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/3.1.3.tar.gz \
    && tar xfz /tmp/redis.tar.gz \
    && rm -r /tmp/redis.tar.gz \
    && mkdir -p /usr/src/php/ext \
    && mv phpredis-3.1.3 /usr/src/php/ext/redis \
    && docker-php-ext-install redis > /dev/null

# don't quite install new relic, but set up apt-get so that we can do it later
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' > /etc/apt/sources.list.d/newrelic.list \
    && curl -L https://download.newrelic.com/548C16BF.gpg | apt-key add \
    && apt-get update
