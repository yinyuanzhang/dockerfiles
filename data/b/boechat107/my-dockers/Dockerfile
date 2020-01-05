#
# Octave Dockerfile
#

# Pull base image.
FROM debian:testing

MAINTAINER Andre Boechat boechat107@gmail.com

# Install Octave
RUN \
  apt-get update -qq
  apt-get install octave octave-image octave-missing-functions octave-nan \
      octave-statistics

# Define default command.
#CMD ["redis-server", "/etc/redis/redis.conf"]

# Expose ports.
#EXPOSE 6379
