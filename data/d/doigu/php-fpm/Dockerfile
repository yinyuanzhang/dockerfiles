# https://hub.docker.com/_/ubuntu/
FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y php7.0-fpm \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/log/php/ /run/php \
    && ln -sf /dev/stderr /var/log/php/error.log
    
COPY php.ini php-fpm.conf /etc/php/7.0/fpm/
COPY www.conf /etc/php/7.0/fpm/pool.d/
    
EXPOSE 9000

CMD ["php-fpm7.0", "--nodaemonize"]