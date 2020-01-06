FROM php:5.5.30-apache
RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng12-dev \
        libicu-dev \
        libmemcached-dev \
        git \
    && cd /etc/apache2/mods-enabled \
    && ln -s ../mods-available/rewrite.load rewrite.load \
    && docker-php-ext-install pdo_mysql mysql mysqli zip mcrypt intl mbstring \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install gd
RUN curl -fsSL 'https://github.com/php-memcached-dev/php-memcached/archive/2.2.0.tar.gz' -o memcached.tar.gz \
    && mkdir -p memcached \
    && tar -xf memcached.tar.gz -C memcached --strip-components=1 \
    && rm memcached.tar.gz \
    && ( \
        cd memcached \
        && phpize \
        && ./configure --enable-memcached \
        && make -j$(nproc) \
        && make install \
    ) \
    && rm -r memcached \
    && echo "extension=/usr/local/lib/php/extensions/no-debug-non-zts-20121212/memcached.so" > /usr/local/etc/php/conf.d/docker-php-ext-memcached.ini
RUN pecl install https://xdebug.org/files/xdebug-2.5.5.tgz \
    && echo "error_reporting = E_ALL" > /usr/local/etc/php/php.ini \
    && echo "display_startup_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "display_errors = On" >> /usr/local/etc/php/php.ini \
    && echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20121212/xdebug.so" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.idekey=\"PHPSTORM\"" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \
    && echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
RUN sed -i 's/\/var\/www\/html/\/var\/www\/web/g' /etc/apache2/apache2.conf \
    && mv /var/www/html /var/www/web
