FROM ubuntu:17.10
MAINTAINER RazzDazz
# Selfmade Docker-Container 
# https://github.com/prometheus/snmp_exporter/tree/master/generator
# 
ENV REFRESHED_AT 2019-01-06
ENV DEBIAN_FRONTEND noninteractive

#
# Preparations
#

# Update packages, install apache, free diskspace
RUN apt-get -yqq update && \
    apt-get -yqq upgrade && \
    apt-get -yqq install build-essential && \
    apt-get -yqq install curl && \
    apt-get -yqq install libsnmp-dev && \
    apt-get -yqq install git && \
    apt-get -yqq install golang && \
    apt-get -yqq install unzip && \
    rm -rf /var/lib/apt/lists/*

#
# Install SNMP Generator
#

RUN go get github.com/prometheus/snmp_exporter/generator && \
    cd ${GOPATH-$HOME/go}/src/github.com/prometheus/snmp_exporter/generator && \
    go build && \
    make mibs
