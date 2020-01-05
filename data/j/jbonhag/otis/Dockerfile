FROM debian:stable

RUN apt-get update
RUN apt-get install curl virtualbox -y; exit 0
RUN curl -OL https://dl.bintray.com/mitchellh/vagrant/vagrant_1.6.5_x86_64.deb
RUN dpkg -i vagrant_1.6.5_x86_64.deb 
