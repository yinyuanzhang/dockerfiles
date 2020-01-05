FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:openjdk-r/ppa

RUN apt-get update
RUN apt-get -y install openjdk-8-jdk
RUN update-alternatives --display java

CMD ["/bin/bash"]
