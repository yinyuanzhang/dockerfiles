FROM gitlab/gitlab-runner
MAINTAINER Huaming Rao <huaming.rao@gmail.com>

RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -
RUN apt-get install -y \
  nodejs \
  python2.7 \
  build-essential

RUN npm install -g strongloop
RUN npm install -g gulp
RUN npm install -g jshint
RUN npm install -g istanbul
RUN npm install -g source-map

RUN ln -s /usr/bin/python2.7 /usr/bin/python

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN npm cache clean
