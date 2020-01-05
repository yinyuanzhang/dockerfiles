FROM ubuntu:17.10
MAINTAINER Sijo K George <cijo_k_george@yahoo.co.in>

SHELL ["/bin/bash", "-c"]
RUN apt-get -y update \
  && apt-get install -y software-properties-common vim \ 
  && add-apt-repository ppa:kivy-team/kivy \ 
  && apt-get install -y python3 python3-kivy python3-pip

ENTRYPOINT ["/bin/bash"]

WORKDIR /root
