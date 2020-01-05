FROM ubuntu:18.04

RUN apt-get -y update
RUN apt-get install -y gpg

COPY pshoepping.asc /root
RUN gpg --import /root/pshoepping.asc
