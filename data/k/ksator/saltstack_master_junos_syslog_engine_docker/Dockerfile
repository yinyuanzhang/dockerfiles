FROM ubuntu:16.04

MAINTAINER Khelil Sator <ksator@juniper.net> 

RUN apt-get update && apt-get install -y wget 
RUN wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | apt-key add -
RUN echo 'deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main' > /etc/apt/sources.list.d/saltstack.list
RUN apt-get update
RUN apt-get install -y salt-master python-pip nano vim tcpdump 
RUN apt-get --auto-remove --yes remove python-openssl 
RUN pip install pyOpenSSL junos-eznc jxmlease jsnapy
RUN pip install pyparsing twisted 
RUN pip install requests nose six rt

