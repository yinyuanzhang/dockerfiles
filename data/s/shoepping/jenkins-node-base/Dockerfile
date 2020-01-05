FROM jenkinsci/ssh-slave

RUN apt-get update
RUN apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     jq \
     software-properties-common

ENV DOCKER_VERSION 5:18.09.6~3-0~debian-stretch

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

RUN apt-get update
RUN apt-cache madison docker-ce
RUN apt-get install -y docker-ce=${DOCKER_VERSION}

RUN usermod -aG docker jenkins

ENV DOCKER_COMPOSE_VERSION=1.24.0

RUN curl -L "https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

RUN chmod +x /usr/local/bin/docker-compose
RUN docker-compose --version
