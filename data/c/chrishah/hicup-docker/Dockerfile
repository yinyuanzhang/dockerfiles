FROM ubuntu:18.04

MAINTAINER <christoph.hahn@uni-graz.at>

RUN apt-get update && apt-get -y upgrade && apt-get install -y build-essential vim git wget python unzip samtools 

WORKDIR /usr/src

#Download Hicup
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/hicup/hicup_v0.7.0.tar.gz && \
tar xvfz hicup_v0.7.0.tar.gz

#install bowtie2
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.4.3/bowtie2-2.3.4.3-linux-x86_64.zip && \
unzip bowtie2-2.3.4.3-linux-x86_64.zip

#Install R (R installation asks for timezone interactively so this needs to be switched off and set before)
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
## preesed tzdata, update package index, upgrade packages and install needed software
# and finally ggplot2 with all dependencies
RUN echo "tzdata tzdata/Areas select Europe" > /tmp/preseed.txt; \
        echo "tzdata tzdata/Zones/Europe select Vienna" >> /tmp/preseed.txt; \
        debconf-set-selections /tmp/preseed.txt && \
        apt-get update && \
        apt-get install -y tzdata r-base

#add bowtie2 and hicup executables to path
ENV PATH="/usr/src/bowtie2-2.3.4.3-linux-x86_64:/usr/src/hicup_v0.7.0:${PATH}"

#create working directory and move to entrypoint
VOLUME /home/data
WORKDIR /home/data
