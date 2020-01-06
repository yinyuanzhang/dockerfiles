FROM kokofirst/docker-php:7.3-fpm-general

RUN pecl install xdebug \
    && docker-php-ext-enable xdebug

# Install Xdebug extension from source
#COPY ./xdebug-2.6.0.tgz /tmp/xdebug.tgz
#RUN mkdir -p /tmp/xdebug \
#    && tar -xf /tmp/xdebug.tgz -C /tmp/xdebug --strip-components=1 \
#    && rm /tmp/xdebug.tgz \
#    && docker-php-ext-configure /tmp/xdebug --enable-xdebug \
#    && docker-php-ext-install /tmp/xdebug \
#    && rm -r /tmp/xdebug