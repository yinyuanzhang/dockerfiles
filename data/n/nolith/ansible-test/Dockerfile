FROM ubuntu-upstart:12.04
MAINTAINER Alessio Caiazza

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y openssh-server python-software-properties apt-transport-https\
  && apt-add-repository -y ppa:ansible/ansible && apt-get update \
  && apt-get install -y ansible \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash -G sudo ansible \
  && echo "ansible:docker" | chpasswd

EXPOSE 22
