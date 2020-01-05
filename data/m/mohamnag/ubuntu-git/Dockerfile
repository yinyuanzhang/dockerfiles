FROM ubuntu:14.04
MAINTAINER Mohammad Naghavi <mohamnag@gmail.com>

ENV COMPOSE_VERSION 1.7.1

RUN apt-get update && \
    apt-get install -y git-core apt-transport-https ca-certificates apparmor curl 

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" > /etc/apt/sources.list.d/docker.list 

RUN apt-get update && \
    apt-get install -y docker-engine && \
    apt-get clean -y

RUN curl -L https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

CMD ["git"]
