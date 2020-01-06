FROM alpine:3.8
LABEL Maintainer="Tim de Pater <code@trafex.nl>" \
      Description="Lightweight container with Nginx 1.14 & PHP-FPM 7.2 based on Alpine Linux."

# Install packages
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/' /etc/apk/repositories \
    && apk update \
        && apk add --no-cache \
        # Install base packages ('ca-certificates' will install 'nghttp2-libs')
        ca-certificates \
        # 1.78 mb
        libressl \
        # # openssh  \
        # # openssl  \
        tzdata \
        pcre \
        # # install php7 and some extensions
        # 9.18mb
        libressl \
        # openssh  \
        # openssl  \
        tzdata \
        pcre \
        # install php7 and some extensions
        php7 \
        php7-fpm php7-pcntl \
        # php7-common \
        php7-bcmath \
        php7-intl \
        php7-curl \
        php7-ctype \
        php7-dom \
        php7-fileinfo \
        # php7-gettext \
        php7-gd \
        php7-iconv \
        # php7-imagick \
        php7-json \
        php7-mbstring \
        php7-mongodb \
        php7-mysqlnd \
        php7-openssl \
        # php7-opcache \
        php7-pdo \
        php7-pdo_mysql \
        php7-pdo_sqlite \
        php7-phar \
        php7-posix \
        php7-redis \
        php7-simplexml \
        php7-sockets \
        php7-sodium \
        # php7-sqlite \
        php7-session \
        php7-sysvshm \
        php7-sysvmsg \
        php7-sysvsem \
        php7-tokenizer \
        php7-zip \
        php7-zlib \
        nginx \
        supervisor \
    && mkdir -p /var/www \
    && adduser -D -g 'www' www \
    && chown -R www:www /var/www \
    && apk del --purge *-dev  \
    && rm -rf /var/cache/apk/* /tmp/* /usr/share/man /usr/share/php7
# Configure nginx
COPY config/nginx.conf /etc/nginx/nginx.conf

# Configure PHP-FPM
COPY config/php-fpm.d/ /etc/php7/php-fpm.d/
COPY config/php.ini /etc/php7/conf.d/zzz_custom.ini

# Configure supervisord
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Add application
WORKDIR /var/www
COPY src/ /var/www

# COPY --from=ochinchina/supervisord:latest /usr/local/bin/supervisord /usr/local/bin/supervisord

EXPOSE 80 443
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
