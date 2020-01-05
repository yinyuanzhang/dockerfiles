FROM ubuntu:16.04
MAINTAINER Tobias Jansen <tobias@tjbn.de>

RUN apt-get update && apt-get upgrade -y
RUN apt-get install openjdk-8-jre icedtea-8-plugin -y

ENTRYPOINT cd /root && ./start.sh
