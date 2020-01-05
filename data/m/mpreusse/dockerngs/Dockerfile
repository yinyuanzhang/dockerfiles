FROM ubuntu:16.04

MAINTAINER Martin Preusse

# set /bin/sh
# necessary for some install scripts calling /bin/sh
RUN rm /bin/sh && ln -s /bin/bash /bin/sh


# install basic packages
RUN apt-get update; \
    apt-get install -y git wget curl gzip perl unzip bzip2 build-essential make libncurses5-dev zlib1g-dev zip ghostscript

RUN mkdir /install
WORKDIR /install


# install Minoconda & BioConda
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh; \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda; \
    rm -Rf Miniconda3-latest-Linux-x86_64.sh;    
ENV PATH "$PATH:/opt/miniconda/bin"
RUN conda config --add channels r; conda config --add channels bioconda;
RUN conda update --yes conda


# Install genomics tools

## Install from Bioconda
RUN conda install --yes bedtools bowtie2 bwa samtools bcftools blat blast tophat fastqc

## Bismarck
RUN mkdir -p /opt/bismarck; \
    wget -q https://github.com/FelixKrueger/Bismark/archive/0.16.3.tar.gz -O bismarck.tar.gz; \    
    tar xzf bismarck.tar.gz; mv Bismark-*/* /opt/bismarck; rm -Rf Bismark-* 
ENV PATH "$PATH:/opt/bismarck"

## Homer
RUN mkdir -p /opt/homer; cd /opt/homer; \
    wget -q http://homer.salk.edu/homer/configureHomer.pl; \
    perl configureHomer.pl -install homer; 
ENV PATH "$PATH:/opt/homer/bin"


# cleanup
WORKDIR /
RUN rm -Rf /install

RUN echo $PATH

# add download script
ADD genome_processing/ /opt/genome_processing/
RUN chmod 755 /opt/genome_processing/*
ENV PATH "$PATH:/opt/genome_processing"
