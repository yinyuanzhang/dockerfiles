FROM ubuntu:14.04.1
MAINTAINER Manuel Durán Aguete "manuel@aguete.org"
RUN apt-get -yqq install wget
RUN echo 'deb http://packages.erlang-solutions.com/ubuntu trusty contrib' > /etc/apt/sources.list.d/esl_erlang.list
RUN wget -O - http://binaries.erlang-solutions.com/debian/erlang_solutions.asc | apt-key add -
RUN apt-get -yqq update
RUN apt-get -yqq upgrade
RUN apt-get -yqq  install  esl-erlang
