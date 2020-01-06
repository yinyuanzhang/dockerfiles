ARG DOCKER_TAG
FROM brumbrum/python3:$DOCKER_TAG as builder
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>

RUN \
 apt-get --no-install-recommends -y install wget gnupg && \
 echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list && \
 wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
 apt-get update && \
 apt-get --no-install-recommends -y install google-chrome-stable && \
 apt-get -y purge gnupg && \
 apt-get -y autoclean && \
 apt-get -y clean && \
 apt-get -y autoremove
