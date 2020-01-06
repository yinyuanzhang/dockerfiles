FROM balenalib/raspberry-pi-alpine

RUN [ "cross-build-start" ]

RUN apk add --no-cache redis && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /data/redis && \
    chown -R redis:redis /data/redis

RUN [ "cross-build-end" ]

COPY raspberry-pi/alpine/redis/redis*.conf /etc/

EXPOSE 6379
CMD ["redis-server", "/etc/redis.conf"]
