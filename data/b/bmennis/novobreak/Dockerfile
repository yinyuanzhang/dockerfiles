FROM ubuntu:18.04

MAINTAINER Brian Ennis

RUN apt-get update && apt-get -y upgrade && apt-get install -y git bc &&\
  git clone https://github.com/czc/nb_distribution.git
ENV PATH="/nb_distribution/:${PATH}"

