FROM jenkins/jenkins:lts
# if we want to install via apt
USER root
RUN curl -fsSL get.docker.com | sh

RUN curl -L --fail https://github.com/docker/compose/releases/download/1.14.0/run.sh > /usr/local/bin/docker-compose
RUN chmod a+x /usr/local/bin/docker-compose

COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

RUN \
  apt-get install -y sudo ; \
  apt-get update && sudo apt-get install -y apt-transport-https ; \
  curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - ; \
  echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list ; \
  apt-get update ; \
  apt-get install -y kubectl ;

USER jenkins
