FROM alpine:3.2
MAINTAINER Didiet Noor <dnoor@kulina.id> (@lynxluna)


# Patch APK Mirror to YKode
RUN echo "https://alpine.ykode.com/alpine/v3.2/main" > /etc/apk/repositories

ENV TIMEZONE Asia/Jakarta
ENV PHP_MEMORY_LIMIT 512M
ENV MAX_UPLOAD 50M
ENV PHP_MAX_FILE_UPLOAD 200
ENV PHP_MAX_POST 100M

RUN apk update && \
  apk add tzdata && \
  cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
  echo "${TIMEZONE}" > /etc/timezone && \
  apk add php-intl \
    php-mcrypt \
    php-openssl \
    php-gmp \
    php-json \
    php-dom \
    php-pdo \
    php-zip \
    php-mysql \
    php-bcmath \
    php-gd \
    php-xcache \
    php-pdo_mysql \
    php-gettext \
    php-xmlreader \
    php-xmlrpc \
    php-bz2 \
    php-memcache \
    php-iconv \
    php-curl \
    php-ctype \
    php-fpm \
    php-phar \
    php && \
  curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/bin --filename=composer && \
  sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/php-fpm.conf && \
  sed -i -e "s/listen\s*=\s*127.0.0.1:9000/listen = 9000/g" /etc/php/php-fpm.conf && \
  sed -i "s|;date.timezone =.*|date.timezone = ${TIMEZONE}|" /etc/php/php.ini && \
  sed -i "s|memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|" /etc/php/php.ini && \
    sed -i "s|upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|" /etc/php/php.ini && \
    sed -i "s|max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|" /etc/php/php.ini && \
    sed -i "s|post_max_size =.*|max_file_uploads = ${PHP_MAX_POST}|" /etc/php/php.ini && \
    sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/php.ini && \
  mkdir /www && \
  apk del tzdata && \
  rm -rf /var/cache/apk/*

EXPOSE 9000


