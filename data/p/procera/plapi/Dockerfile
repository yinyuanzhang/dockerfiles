FROM python:2.7 
MAINTAINER Peter Salanki <peter.salanki@proceranetworks.com>

WORKDIR /tmp

RUN wget http://download.proceranetworks.com/pldownload/python/plapi/.builds/18.1.0py1/plapi-18.1.0py1-py2.7-linux-x86_64.egg
RUN easy_install plapi-18.1.0py1-py2.7-linux-x86_64.egg
RUN rm plapi-18.1.0py1-py2.7-linux-x86_64.egg
