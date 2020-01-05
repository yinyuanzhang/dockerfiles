FROM phusion/baseimage:latest
MAINTAINER Irakli Nadareishvili

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get -yqq update
RUN apt-get install -yqq curl

RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo -E bash -
RUN apt-get install -yqq nodejs

# Standard clean-up for the baseimage. @see: http://phusion.github.io/baseimage-docker/
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
