#################################################################
# Dockerfile
#
# Software:         FastQC
# Version:          v0.0.1
# Description:      Tool to spot potential problems in high througput sequencing datasets 
# Website:          http://www.bioinformatics.babraham.ac.uk/projects/fastqc
# Provides:         FastQC 0.11.8
# Base Image:       ubuntu:18.04
# Build Cmd:        docker build --rm -t cwlhub/fastqc:v0.0.1 .
# Pull Cmd:         docker pull cwlhub/fastqc:v0.0.1
# Run Cmd:          docker run --rm -ti cwlhub/fastqc:v0.0.1 fastqc --version
#################################################################

### Base Image
FROM ubuntu:18.04
LABEL maintainer="misha.kotliar@gmail.com"
ENV DEBIAN_FRONTEND noninteractive

################## BEGIN INSTALLATION ######################

WORKDIR /tmp

ENV VERSION 0.11.8
ENV NAME fastqc
ENV URL "http://www.bioinformatics.babraham.ac.uk/projects/fastqc/${NAME}_v${VERSION}.zip"

### Installing dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        unzip \
        binutils \
        libfindbin-libs-perl \
        openjdk-11-jdk && \
### Installing FastQC
    wget -q -O /opt/${NAME}_v${VERSION}.zip $URL && \
    cd /opt && \
    unzip ./${NAME}_v${VERSION}.zip &&\
    chmod 777 /opt/FastQC/${NAME} && \
    ln -s /opt/FastQC/${NAME} /usr/local/bin/ &&\
    rm /opt/${NAME}_v${VERSION}.zip &&\
### Cleaning
    apt-get clean && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/* && \
    strip /usr/local/bin/*; true