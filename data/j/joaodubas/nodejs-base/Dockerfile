# base image for nodejs
#
# VERSION: see `TAG`
FROM debian:jessie
MAINTAINER Joao Paulo Dubas "joao.dubas@gmail.com"

# update dependencies
RUN apt-get -y -qq --force-yes update \
    && apt-get -y -qq --force-yes install git build-essential wget python

# cleanup temp files
RUN apt-get -y -qq --force-yes clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# configure execution
CMD ["node"]
