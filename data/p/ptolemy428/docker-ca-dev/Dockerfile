FROM ubuntu:14.04
MAINTAINER Larry Liang <ptolemy428@gmail.com>

#Install latest ansible
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | sudo tee -a /etc/apt/sources.list
RUN echo "deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | sudo tee -a /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y --force-yes install ansible

#Install dev tools
RUN apt-get -y install python-pip \
    curl
RUN pip install yapf
