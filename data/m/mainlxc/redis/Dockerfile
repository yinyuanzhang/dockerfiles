FROM redis:5.0
RUN mkdir -p /usr/local/etc/redis
RUN ln -s /var/run/secrets/redis.conf /usr/local/etc/redis/redis.conf 
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]