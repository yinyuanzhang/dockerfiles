FROM obada/nginx-fpm
MAINTAINER Andrii Tarykin <ksbomj@gmail.com>

COPY ./etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY ./etc/php7/php-fpm.d/www.conf /etc/php7/php-fpm.d/www.conf
COPY ./etc/php7/php-fpm.conf /etc/php7/php-fpm.conf

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY src /app
WORKDIR /app

CMD ["/docker-entrypoint.sh"]
