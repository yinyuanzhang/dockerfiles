FROM centos

MAINTAINER Eylul Akbas <eylul.akbas@sekom.com.tr>

WORKDIR /home/plapi17

RUN yum -y upgrade
RUN yum -y install wget
RUN yum -y install python-setuptools
RUN wget http://download.proceranetworks.com/pldownload/python/plapi/.builds/17.2.0py1/plapi-17.2.0py1-py2.7-linux-x86_64.egg
RUN easy_install plapi-17.2.0py1-py2.7-linux-x86_64.egg
