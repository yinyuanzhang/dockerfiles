# DOCKER-VERSION 0.7.1
FROM      ubuntu:14.04.3
MAINTAINER Adam Kaczmarczyk <kaczmarczyk.a@gmail.com>

# make sure the package repository is up to date
#RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install build-essential

# install python-software-properties (so you can do add-apt-repository)
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-properties software-properties-common

# install SSH server so we can connect multiple times to the container
RUN apt-get -y install openssh-server && mkdir /var/run/sshd

# install oracle java from PPA
RUN add-apt-repository ppa:webupd8team/java -y
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get -y install oracle-java8-installer && apt-get clean

# Set oracle java as the default java
RUN update-java-alternatives -s java-8-oracle
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

# install utilities
RUN apt-get -y install vim git sudo zip bzip2 fontconfig curl

# install maven
RUN apt-get -y install maven

# configure the "ubuntu" and "root" users
RUN echo 'root:ubuntu' |chpasswd
RUN groupadd ubuntu && useradd ubuntu -s /bin/bash -m -g ubuntu -G ubuntu && adduser ubuntu sudo
RUN echo 'ubuntu:ubuntu' |chpasswd

# expose the SSHD port, and run SSHD

EXPOSE	22
CMD    /usr/sbin/sshd -D