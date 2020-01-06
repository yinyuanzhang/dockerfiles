FROM jenkins:2.60.3
MAINTAINER Rene Meza <rene.meza125@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

# Change to root user
USER root

# Arg for the docker group ID
ARG DOCKER_GID=497

# Create docker group with GID
RUN groupadd -g ${DOCKER_GID:-497} docker

# Install supporting packages
RUN apt-get update -y && \
    apt-get install apt-transport-https curl python-dev python-setuptools \
    gcc make libssl-dev -y && \
    easy_install pip

# Args to control Docker and Docker Compose versions
ARG DOCKER_ENGINE=1.11.0
ARG DOCKER_COMPOSE=1.9.0

# Install Docker Engine
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D && \
    echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee /etc/apt/sources.list.d/docker.list && \
    apt-get update -y && \
    apt-get purge lxc-docker* -y && \
    apt-get install docker-engine=${DOCKER_ENGINE:-1.11.0}-0~xenial -y && \
    usermod -aG docker jenkins && \
    usermod -aG users jenkins

# Install Docker Compose
RUN pip install docker-compose==${DOCKER_COMPOSE:-1.9.0} && \
    pip install ansible boto boto3

# Change to jenkins user
USER jenkins

# COPY config/ssh/* /var/jenkins_home/.shh/

# add executors
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy

# Add Jenkins plugins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt
