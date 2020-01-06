FROM jenkins/jenkins:lts
LABEL maintainer="Hugo Josefson <hugo@josefson.org> (https://www.hugojosefson.com)"

USER root
RUN (echo "deb http://deb.debian.org/debian stretch-backports main" >> /etc/apt/sources.list) \
  && apt-get update \
  && apt-get -t stretch-backports dist-upgrade -y \
  && apt-get -t stretch-backports install -y vim libltdl7 \
  && rm -rf /var/lib/apt/lists/*

USER jenkins
