FROM dacr/jenkins-slave
MAINTAINER crosson.david@gmail.com

RUN curl -sSL https://get.docker.com/ | sh

RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
 && chmod +x /usr/local/bin/docker-compose

