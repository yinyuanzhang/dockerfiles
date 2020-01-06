FROM ubuntu:trusty

MAINTAINER Andy McGrath (apextc)

#Update uBuntu and install apps needed for build
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update
RUN apt-get install python2.7 python-pip ansible -y
RUN pip2 install f5-sdk
RUN pip2 install netaddr
RUN pip2 install suds
RUN pip2 install bigsuds
RUN pip2 install boto
RUN pip2 install botocore
RUN pip2 install boto3
RUN pip2 install paramiko
RUN ansible --version

#System clean-up
RUN apt-get autoclean
RUN apt-get clean
