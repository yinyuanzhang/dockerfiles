FROM jenkins/jenkins
LABEL maintainer="Todd Edwards <todd@mtn.cc>"
LABEL github="https://github.com/triangletodd/docker-jenkins-for-volumes"
LABEL dockerhub="https://hub.docker.com/r/todd/jenkins-for-volumes/"

USER root
ENV GPG_KEY B42F6819007F00F88E364FD4036A9C25BF357DD4

# gosu
RUN curl -sSL -o /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.11/gosu-$(dpkg --print-architecture)" \
  && chmod +x /usr/local/bin/gosu

COPY volume-permissions.sh /usr/local/bin/volume-permissions.sh

ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/volume-permissions.sh"]
