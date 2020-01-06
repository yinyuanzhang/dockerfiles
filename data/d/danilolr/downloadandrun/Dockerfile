FROM ubuntu:16.04

MAINTAINER Danilo Luiz Rheinheimer

RUN apt-get update 
RUN apt-get install -y nano wget

RUN mkdir /opt/app
COPY run.sh /opt/app
WORKDIR /opt/app
CMD /opt/app/run.sh