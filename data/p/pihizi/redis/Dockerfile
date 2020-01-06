FROM debian:7.6
MAINTAINER pihizi@msn.com

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y redis-server && \
    sed -i 's/^\(bind .*\)$/# \1/' /etc/redis/redis.conf && \
    sed -i 's/^\(daemonize .*\)$/# \1/' /etc/redis/redis.conf && \
    sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf

# VOLUME ["/data", "/etc/redis", "/var/log/redis"]

EXPOSE 6379

CMD ["/usr/bin/redis-server", "/etc/redis/redis.conf"]
