FROM        eadz/ubuntu-trusty-base:latest
MAINTAINER _@eaden.net
RUN         apt-get update && apt-get upgrade -y
RUN         apt-get -y install redis-server
EXPOSE      6379
ENTRYPOINT  ["/usr/bin/redis-server"]
