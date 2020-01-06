FROM ubuntu:17.04

RUN apt-get update && \
    apt-get install -y wget bash unzip

WORKDIR /tmp
RUN wget -O packer.zip https://releases.hashicorp.com/packer/1.1.1/packer_1.1.1_linux_amd64.zip
WORKDIR /opt/packer
RUN unzip /tmp/packer.zip
RUN ln -s /opt/packer/packer /usr/local/bin/