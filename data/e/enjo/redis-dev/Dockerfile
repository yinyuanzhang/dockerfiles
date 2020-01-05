FROM redis:4.0.14

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
apt-get -y install bbe && \
bbe -e 's/4.0.14/2.2.12/' /usr/local/bin/redis-server >/usr/local/bin/redis-server-adjusted && \
chmod +x /usr/local/bin/redis-server-adjusted

COPY redis.conf /usr/local/etc/redis/redis.conf

CMD [ "redis-server-adjusted", "/usr/local/etc/redis/redis.conf" ]
