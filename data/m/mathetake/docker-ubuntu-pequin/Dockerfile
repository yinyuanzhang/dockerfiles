FROM ubuntu:latest
MAINTAINER @mathetake

RUN apt-get update
RUN apt-get install -y git sudo
RUN git clone https://github.com/pepper-project/pequin

WORKDIR pequin
RUN yes | ./install_debian_ubuntu.sh
