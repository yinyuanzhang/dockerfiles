FROM alpine:3.10

LABEL Maintainer="Murat Bağsız <murat@bagsiz.com>"

# Set timezone -> Istanbul/Turkey
RUN apk --update add tzdata
RUN cp /usr/share/zoneinfo/Turkey /etc/localtime
RUN echo "Turkey" >  /etc/timezone
RUN apk del tzdata
RUN date

# Packages
RUN apk --update add \
    bash \
    nginx \
    supervisor \
    git \
    curl \
    unzip \
    nano \
    wget \
    gzip \
    openssl \
    zlib \
    php7 \
    php7-bcmath \
    php7-ctype \
    php7-curl \
    php7-dom \
    php7-fileinfo \
    php7-fpm \
    php7-gd \
    php7-iconv \
    php7-json \
    php7-ldap \
    php7-mbstring \
    php7-mcrypt \
    php7-mysqli \
    php7-mysqlnd \
    php7-opcache \
    php7-openssl \
    php7-pcntl \
    php7-pdo \
    php7-pdo_mysql \
    php7-phar \
    php7-posix \
    php7-redis \
    php7-session \
    php7-simplexml \
    php7-tokenizer \
    php7-xml \
    php7-xmlreader \
    php7-xmlwriter \
    php7-zip \
    php7-zlib

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

# Default Nginx
COPY src/nginx.conf /etc/nginx/nginx.conf

# Default PHP-FPM
COPY src/fpm-pool.conf /etc/php7/php-fpm.d/docker_custom.conf
COPY src/php.ini /etc/php7/conf.d/docker_custom.ini

# Configure supervisord
COPY src/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Laravel Nginx configuration
COPY src/nginx-default /etc/nginx/sites-available/default
WORKDIR /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

# Application
RUN rm -rf /var/www
RUN mkdir -p /var/www
WORKDIR /var/www
COPY src/ /var/www/

# Cleanup
RUN rm -rf /var/cache/apk
RUN rm -rf /root/.composer/cache

EXPOSE 8080
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
