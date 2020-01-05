FROM openjdk:8u212-jdk-stretch
MAINTAINER Alan Giles <alan.giles@boxever.com>

RUN apt-get update
RUN apt-get install -y python-pip=9.0.1-2
RUN pip install boto3==1.9.134
RUN pip install awscli==1.16.144
RUN apt-get clean
