FROM ubuntu:16.04

# install system packages
RUN apt dist-upgrade --assume-yes
RUN apt-get update --quiet
RUN apt install --yes software-properties-common
RUN add-apt-repository --yes ppa:ubuntu-toolchain-r/test
RUN apt update --quiet
RUN apt install --quiet --yes cloc cmake doxygen git libboost-dev ninja-build
