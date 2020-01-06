FROM ubuntu:18.04
MAINTAINER sih4sing5hong5


RUN apt-get update -qq && \
  apt-get install -y g++ make

WORKDIR /opt
COPY srilm-1.7.2.tar.gz .
RUN tar -xzf srilm-1.7.2.tar.gz
RUN sed '5iSRILM=/opt' -i Makefile
RUN make

WORKDIR /opt/bin/i686-m64/
