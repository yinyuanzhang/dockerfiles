FROM alpine:3.6

LABEL Maintainer="Devops <devops@goxip.com>" \
      Description="Lightweight container with Nginx 1.12 & PHP-FPM 7.1 based on Alpine Linux."

# Add PHP Repo
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-alpine.rsa.pub
RUN echo "http://php.codecasts.rocks/v3.6/php-7.1" >> /etc/apk/repositories

# Install packages
RUN apk update && apk upgrade && \ 
    apk --no-cache add --update \
    libressl libressl-dev libssl1.0 libmcrypt-dev nginx supervisor curl

# Install PHP
RUN apk --no-cache add --update \
    php7 php7-common php7-fpm php7-mysqli php7-pdo php7-pdo_mysql php7-json php7-openssl \
    php7-curl php7-zlib php7-xml php7-phar php7-intl php7-dom php7-ctype php7-opcache \
    php7-mbstring php7-gd php7-mcrypt php7-redis php7-xsl php7-xml php7-xmlreader \
    php7-iconv php7-gettext php7-bz2 php7-zip php7-ftp php7-openssl php7-imagick php7-memcached \
    php7-mongodb php7-xdebug
    
# Clean up
RUN mkdir /var/log/supervisor && \
    rm -rf /var/cache/apk/*

# add user www-data
#RUN adduser -S www-data
RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1

# Nginx configuration
RUN rm /etc/nginx/conf.d/*
COPY config/nginx.conf /etc/nginx/nginx.conf

# PHP configuration
RUN rm /etc/php7/php-fpm.d/www.conf
COPY config/php-fpm.conf /etc/php7/php-fpm.conf
COPY config/php.ini /etc/php7/php.ini

# Configure supervisord
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Init script
COPY init_script.sh /init_script.sh
RUN chmod +x /init_script.sh

CMD ["/bin/sh", "/init_script.sh"]