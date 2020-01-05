# -----------------------------------------------------------------------------
# docker-java8-base
#
# Base image for use in my java8 images
#
# This is a rework of my images, using this as an intermediate for my
# existing Minecraft images
#
# Authors: Brian Eilber
# Updated: August 18th, 2017
# Require: Docker (http://www.docker.io/)
# -----------------------------------------------------------------------------


FROM    ubuntu:16.04

MAINTAINER Brian Eilber <brian.eilber@gmail.com>

ENV     DEBIAN_FRONTEND noninteractive

RUN     apt-get --yes update && \
        apt-get --yes upgrade && \
        apt-get --yes install software-properties-common

RUN     add-apt-repository ppa:webupd8team/java && apt-get --yes update
RUN     echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
        echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
        apt-get --yes install oracle-java8-installer && \
        apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

