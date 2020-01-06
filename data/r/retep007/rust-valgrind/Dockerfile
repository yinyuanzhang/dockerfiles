FROM ubuntu:18.04

MAINTAINER retep007

RUN apt-get -y update

# create volume
RUN mkdir -p /root/build
VOLUME /root/build

# Fix non interactive bug in Tzdata https://bugs.launchpad.net/ubuntu/+source/tzdata/+bug/1554806
RUN ln -fs /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime
RUN apt-get -y install build-essential valgrind git-all curl
RUN apt-get -y clean
# Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH "$PATH:/root/.cargo/bin"
