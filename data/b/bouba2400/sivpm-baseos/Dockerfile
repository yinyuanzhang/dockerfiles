FROM phusion/baseimage

ENV HOME /root
ENV LANG en_US.UTF-8
RUN locale-gen en_US.UTF-8

RUN apt-get update -q 2 && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https ca-certificates > /dev/null
    
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y dos2unix

