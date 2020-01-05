#
# Redis Dockerfile in CentOS 7 image
#

# Build:
# docker build -t antik486/centos71
#
# Create:
# docker create -it -p 6379:6379 --name container-redis zokeber/redis
#
# Start:
# docker start container-redis
#
# Connect with redis client
# docker exec -it container-redis redis-cli
#
# Connect bash
# docker exec -it container-redis bash

# Pull base image
FROM antik486/centos71

# Maintener
MAINTAINER Kerim Bekberov <bekberovkerim@gmail.com>


# Install REDIS v2.8

RUN  \
     yum install -y logrotate systemd  \
                    http://dl.fedoraproject.org/pub/epel/7/x86_64/j/jemalloc-3.6.0-1.el7.x86_64.rpm \
                    http://dl.fedoraproject.org/pub/epel/7/x86_64/r/redis-2.8.19-2.el7.x86_64.rpm && \
     rm -r  /var/tmp/* && \
     yum clean all


# Copy config redis
ADD etc/redis.conf /etc/redis.conf

# User
USER root

# Mountable directories
VOLUME ["/var/lib/redis", "/var/log/redis"]

# Set the environment variables
ENV HOME /var/lib/redis

# Working directory
WORKDIR /var/lib/redis

CMD ["/usr/bin/redis-server", "/etc/redis.conf"]

# Expose ports.
EXPOSE 6379
