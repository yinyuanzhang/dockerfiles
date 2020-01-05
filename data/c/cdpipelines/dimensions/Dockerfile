FROM alpine:3.9

# Install packages
RUN apk --no-cache add \
    nginx supervisor curl \
    php7 php7-fpm \
    php7-pdo_mysql php7-pdo_pgsql \
    php7-fileinfo php7-dom php7-xmlreader php7-simplexml php7-zip php7-gd \
    php7-json php7-curl php7-soap php7-xml \
    php7-mbstring php7-mcrypt php7-iconv \
    php7-openssl php7-phar php7-intl \
    php7-zlib php7-dom php7-xmlreader php7-ctype \
    php7-session php7-opcache php7-tokenizer php7-xmlwriter \
    sqlite \
    php7-sqlite3 \
    php7-pdo_sqlite \
    imagemagick php7-imagick

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer

# Configure nginx
COPY ./config/gzip.conf /etc/nginx/gzip.conf
COPY ./config/nginx.conf /etc/nginx/nginx.conf

# Configure PHP-FPM
COPY ./config/fpm-pool.conf /etc/php7/php-fpm.d/zzz_custom.conf
COPY ./config/php.ini /etc/php7/conf.d/zzz_custom.ini

# Configure supervisord
COPY ./config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Clean up Cache
RUN rm -rf /var/cache/apk/*

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
  && ln -sf /dev/stderr /var/log/nginx/error.log

# Add application
RUN mkdir -p /var/www
WORKDIR /var/www

EXPOSE 80 443
