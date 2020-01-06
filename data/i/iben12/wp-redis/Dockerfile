FROM wordpress

RUN printf "\n" | pecl install redis

RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini

