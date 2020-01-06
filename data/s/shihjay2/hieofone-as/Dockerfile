FROM php:fpm-alpine

LABEL Maintainer Michael Shihjay Chen <shihjay2@gmail.com>

# Add Repositories
RUN rm -f /etc/apk/repositories &&\
    echo "http://dl-cdn.alpinelinux.org/alpine/v3.9/main" >> /etc/apk/repositories && \
    echo "http://dl-cdn.alpinelinux.org/alpine/v3.9/community" >> /etc/apk/repositories

# Add Build Dependencies
RUN apk add --no-cache --virtual .build-deps \
    zlib-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libxml2-dev \
    php7-dev \
    autoconf \
    gcc \
    g++ \
    make \
    pcre-dev \
    bzip2-dev

# Add Production Dependencies
RUN apk add --update --no-cache \
    jpegoptim \
    pngquant \
    optipng \
    supervisor \
    nano \
    icu-dev \
    mariadb-client \
    imagemagick-dev \
    libssh2-dev \
    libzip-dev \
    imap-dev \
    libtool \
    freetype-dev

# Configure & Install Extension
RUN docker-php-ext-configure \
    opcache --enable-opcache &&\
    docker-php-ext-configure gd --with-freetype --with-jpeg &&\
    PHP_OPENSSL=yes docker-php-ext-configure imap --with-imap --with-imap-ssl &&\
    docker-php-ext-install \
    opcache \
    mysqli \
    pdo \
    pdo_mysql \
    sockets \
    json \
    intl \
    gd \
    xml \
    zip \
    bz2 \
    pcntl \
    soap \
    imap \
    bcmath

# imagick
RUN pecl install imagick &&\
    docker-php-ext-enable imagick

# Cleanup
RUN apk del .build-deps

# Copy composer.lock and composer.json
COPY composer.lock composer.json /var/www/as/

WORKDIR "/var/www/as"

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
ENV COMPOSER_ALLOW_SUPERUSER=1
ENV PATH="./vendor/bin:$PATH"

# Copy source files and run composer
COPY . /var/www/as
RUN mkdir /var/www/as/vendor

# Copy existing application directory permissions
COPY --chown=www-data:www-data . /var/www/as
RUN chmod 777 /var/www/as/storage
RUN chmod 777 /var/www/as/public
RUN chmod 777 /var/www/as/vendor

USER www-data

# Install all PHP dependencies
RUN composer install --no-interaction

USER root

COPY docker-entrypoint.sh /usr/local/bin/
RUN ["chmod", "+x", "/usr/local/bin/docker-entrypoint.sh"]

COPY supervisord.conf /etc/supervisord.conf
COPY schedule.sh /usr/local/bin/schedule.sh
RUN ["chmod", "+x", "/usr/local/bin/schedule.sh"]

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

EXPOSE 9000
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
