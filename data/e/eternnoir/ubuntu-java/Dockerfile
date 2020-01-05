#
# Ubuntu 14.04 with Java
#
# Pull base image.
FROM ubuntu:14.04
MAINTAINER Frank Wang "eternnoir@gmail.com"

#update
RUN apt-get -y update && apt-get upgrade && apt-get clean
RUN apt-get -y install software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/java 
RUN apt-get -y update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean
