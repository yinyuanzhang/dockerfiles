FROM redis:5.0.7

# 时区
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone

COPY conf/redis.conf /usr/local/etc/redis/redis.conf

EXPOSE 6379

CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]