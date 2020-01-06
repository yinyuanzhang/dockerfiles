FROM jruby:1.7
MAINTAINER "Miguel Mendes Ruiz" <miguel@99taxis.com>

RUN \
  apt-get update && \
  apt-get install -y git && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /var/tmp/*
