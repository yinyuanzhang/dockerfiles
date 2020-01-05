FROM ubuntu:quantal
MAINTAINER Kyle Mathews "mathews.kyle@gmail.com"

RUN apt-get update
RUN apt-get install -y redis-server

EXPOSE 6379
ENTRYPOINT ["/usr/bin/redis-server"]
