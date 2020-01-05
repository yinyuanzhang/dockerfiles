FROM redis:5-alpine3.8

COPY redis.conf /etc/redis/redis.conf

RUN mkdir /var/lib/redis && chown redis:redis /var/lib/redis
VOLUME /var/lib/redis

CMD [ "redis-server", "/etc/redis/redis.conf" ]
