FROM mongo:3.6.11-xenial
RUN echo exit 0 > /usr/sbin/policy-rc.d; \
apt-get update; \
apt-get upgrade -y; \
apt-get install -y --no-install-recommends redis-server redis-tools; \
sed -i 's/^bind 127.0.0.1/bind 0.0.0.0/g' /etc/redis/redis.conf; \
update-rc.d redis-server defaults
EXPOSE 6379
ENTRYPOINT []
CMD service redis-server restart && docker-entrypoint.sh mongod
