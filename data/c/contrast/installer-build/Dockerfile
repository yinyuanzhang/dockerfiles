FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install gcc make openjdk-8-jdk-headless python python-pip \
        build-essential debhelper autotools-dev autoconf automake libtool git \
        lsb-release devscripts equivs sudo apt-transport-https -y && \
    pip install boto3
