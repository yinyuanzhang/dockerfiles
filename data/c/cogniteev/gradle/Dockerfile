FROM java:8
MAINTAINER Cogniteev <tech@cogniteev.com>

ENV VERSION=4.4

RUN apt-get update && wget -q \
  https://services.gradle.org/distributions/gradle-${VERSION}-bin.zip \
  -O /tmp/gradle-${VERSION}-bin.zip && \
  apt-get install -y stow unzip && \
  cd /usr/local/stow/ && unzip /tmp/gradle-${VERSION}-bin.zip && \
  stow gradle-${VERSION} && \
  apt-get purge -y stow unzip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
