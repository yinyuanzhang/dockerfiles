FROM ubuntu:14.04

MAINTAINER Andrei Gladkyi <arg@arglabs.net>

ENTRYPOINT ["/bin/bash", "-l", "-c"]

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN apt-get update
RUN apt-get install -y software-properties-common

RUN add-apt-repository -y ppa:chris-lea/node.js
RUN apt-get update
RUN apt-get install -y git-core curl nodejs phantomjs

RUN curl -sSL https://get.rvm.io | bash -s stable
RUN echo "source /usr/local/rvm/scripts/rvm" >> /etc/bash.bashrc
ADD gemrc /etc/gemrc

RUN /bin/bash -l -c "rvm install 2.1.3"
RUN /bin/bash -l -c "rvm --default use 2.1.3"
