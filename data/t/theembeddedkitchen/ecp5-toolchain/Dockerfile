FROM ubuntu:latest

LABEL maintainer="abhishek@theembeddedkitchen.net"

RUN mkdir /opt/fpga_toolchain
RUN apt-get update
RUN apt-get install -y wget build-essential git
RUN wget https://github.com/xobs/ecp5-toolchain/releases/download/v1.6.1/ecp5-toolchain-linux_x86_64-v1.6.1.tar.gz
RUN tar -xzvf ecp5-toolchain-linux_x86_64-v1.6.1.tar.gz -C /opt/fpga_toolchain
RUN rm -r ecp5-toolchain-linux_x86_64-v1.6.1.tar.gz
