# Pull base image.
FROM debian:stable

# Install Redis.
RUN \
  apt-get update && \
  apt-get -y install apt-utils gcc make wget telnet && \
  cd /tmp && \
  wget http://download.redis.io/redis-stable.tar.gz && \
  tar xvzf redis-stable.tar.gz && \
  cd redis-stable && \
  make && \
  make install && \
  cp -f src/redis-sentinel /usr/local/bin && \
  mkdir -p /etc/redis && \
  cp -f *.conf /etc/redis && \
  rm -rf /tmp/redis-stable* && \
  sed -i 's/6379/6380/g' /etc/redis/redis.conf && \
  sed -i 's/protected-mode yes/protected-mode no/g' /etc/redis/redis.conf && \
  sed -i 's/^\(bind .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(daemonize .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(dir .*\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \
  sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["redis-server", "/etc/redis/redis.conf"]

# Expose ports.
EXPOSE 6380

#docker container run --rm -p 6380:6380 --sysctl net.core.somaxconn=511 husonet/redis-6380
#docker network create redis
#docker container run -it --network redis --network-alias redis-cache --sysctl net.core.somaxconn=511 husonet/redis-6380
#docker container run -d  -it --network redis --network-alias rediscache --sysctl net.core.somaxconn=511 husonet/redis-6380
