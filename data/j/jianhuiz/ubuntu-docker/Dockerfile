FROM ubuntu:14.04

MAINTAINER jianhuiz

RUN apt-get update && apt-get install -y openssh-server cloud-init
RUN mkdir /var/run/sshd

EXPOSE 22
CMD cloud-init init && /usr/sbin/sshd -D

