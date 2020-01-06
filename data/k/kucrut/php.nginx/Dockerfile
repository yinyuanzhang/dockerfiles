FROM php:7.2-fpm-alpine

LABEL Maintainer="Dzikri Aziz <kvcrvt@gmail.com>" \
      Description="Minimalist Nginx 1.12 & PHP 7.2 container on Alpine Linux."

# Install packages
RUN apk add --update nginx supervisor shadow bash && \
    rm -fr /var/cache/apk/*

# Configure nginx
COPY config/nginx/nginx.conf          /etc/nginx/nginx.conf
COPY config/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY config/php-fpm.d/global.conf     /usr/local/etc/php-fpm.d/zzz-global.conf
COPY config/php-fpm.d/www.conf        /usr/local/etc/php-fpm.d/zzz-www.conf

# Fix nginx's temp dir ownership
RUN chown -R www-data:www-data /var/tmp/nginx

# HTML files volume
COPY index.php /var/www/html/index.php
WORKDIR /var/www/html

# Configure supervisord
COPY config/supervisor /etc/supervisor

EXPOSE 80
EXPOSE 443

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
