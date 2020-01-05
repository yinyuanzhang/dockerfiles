FROM jenkins/jenkins:latest
USER root
RUN apt-get update \
  && apt-get install -y curl ca-certificates \
  && curl -s https://get.docker.com/ | sed 's/docker-engine/docker-engine=%%DOCKER_VERSION%%*/' | sh \
  && echo 'DOCKER_OPTS="-H :2375 -H unix:///var/run/docker.sock"' >> /etc/default/docker \
  && apt-get install -y sudo \
  && rm -rf /var/lib/apt/lists/* \
  && echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
USER jenkins
