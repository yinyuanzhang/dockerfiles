FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean && apt-get -y install gcc-8 g++-8 wget make openjdk-11-jre-headless git nasm curl libasound2-dev python

RUN wget https://dl.bintray.com/aeon-engine/aeon_dependencies/cmake/linux/cmake_3.14.2.tar.gz
RUN tar xf cmake_3.14.2.tar.gz

ENV PATH="/cmake_3.14.2/bin:${PATH}"
ENV CC=gcc-8
ENV CXX=g++-8
