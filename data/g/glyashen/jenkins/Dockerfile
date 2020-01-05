FROM jenkins:1.651.2

USER root
RUN apt-get update \
      && apt-get install -y sudo \
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers
RUN curl -L https://get.docker.com/builds/Linux/x86_64/docker-1.10.3 >\
 /usr/bin/docker && chmod +x /usr/bin/docker
USER jenkins