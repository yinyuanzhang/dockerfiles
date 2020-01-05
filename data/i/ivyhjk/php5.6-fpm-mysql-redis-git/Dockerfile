FROM ivyhjk/php5.6-fpm-mysql-git

RUN apk update

RUN curl -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/4.2.0.tar.gz \
    && tar xfz /tmp/redis.tar.gz \
    && rm -r /tmp/redis.tar.gz \
    && mkdir -p /usr/src/php/ext \
    && mv phpredis-* /usr/src/php/ext/redis

RUN docker-php-ext-install redis
