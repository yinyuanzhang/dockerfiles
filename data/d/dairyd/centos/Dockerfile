FROM centos:7

LABEL maintainer="7of9@ydevops.com"

ENV REFRESHED_AT 2019-10-10

RUN yum update -y && yum clean all

RUN mkdir -p /opt/server

ENV HOME /opt/server
WORKDIR /opt/server

VOLUME ["/etc", "/var/log", "/home", "/root"]
