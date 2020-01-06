FROM redis:4.0.11-alpine
# set mainainer
LABEL maintainer="Grokon"
# copy configs
COPY conf/redis.conf /usr/local/etc/redis/redis.conf
# Define default command.
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]