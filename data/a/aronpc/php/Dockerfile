FROM php:7.3-fpm-alpine
LABEL MAINTAINER="ARON PEYROTEO"

RUN apk update
RUN apk upgrade
RUN apk add --update --no-cache \
	sudo \
	libpng-dev \
    php7-mcrypt \
    php7-soap \
    php7-openssl \
    php7-gmp \
#    php7-pdo_odbc \
    php7-json \
    php7-dom \
    php7-pdo \
    php7-zip \
    php7-mysqli \
    php7-sqlite3 \
#    php7-pdo_pgsql \
    php7-bcmath \
    php7-gd \
#    php7-odbc \
    php7-pdo_mysql \
#    php7-pdo_sqlite \
    php7-gettext \
    php7-xmlreader \
    php7-xmlrpc \
    php7-bz2 \
    php7-iconv \
#    php7-pdo_dblib \
    php7-curl \
    php7-session \
    php7-fpm \
    php7-ctype \
    php7-tokenizer

RUN docker-php-ext-install gd tokenizer

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php --quiet --no-ansi --filename=composer --install-dir=/usr/local/bin/
RUN php -r "unlink('composer-setup.php');"

# Configure PHP-FPM
ADD config/fpm-pool.conf /etc/php7/php-fpm.d/www.conf
ADD config/php.ini /etc/php7/conf.d/zzz_custom.ini

RUN echo 'abc ALL=NOPASSWD: ALL' > /etc/sudoers.d/abc

# CLEAN FILES
RUN rm -rf /var/cache/apk/*
RUN rm -rf /src

RUN addgroup abc -g ${GID:-1000}
RUN adduser abc -u ${UID:-1000} -D -h /app -G abc

RUN mkdir /.config
RUN mkdir /.composer

RUN chown abc:abc /usr/local/bin/composer
RUN chown -R abc:abc /.config
RUN chown -R abc:abc /.composer

VOLUME /.config
VOLUME /.composer

# Switch to use a non-root user from here on
USER abc

WORKDIR "/app"

EXPOSE 9000