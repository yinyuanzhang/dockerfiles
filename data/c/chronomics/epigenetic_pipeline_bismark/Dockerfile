#################### BASE IMAGE ######################
FROM ubuntu:16.04

#################### MAINTAINER ######################
MAINTAINER Daniel E. Martin-Herranz <daniel@chronomics.co.uk>

################## INSTALLATION ######################
WORKDIR /usr/local/bin

## General tools

RUN apt-get update -y && apt-get install -y wget unzip build-essential openjdk-8-jre python-setuptools curl zlib1g-dev cmake libjsoncpp-dev libncurses5-dev libncursesw5-dev autoconf libbz2-dev liblzma-dev libcurl4-openssl-dev libssl-dev && easy_install pip && pip install --upgrade pip

## FastQC v0.11.7

ENV DST=/tmp/
ENV URL=http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
ENV ZIP=fastqc_v0.11.7.zip
RUN wget $URL/$ZIP -O $DST/$ZIP && unzip - $DST/$ZIP -d $DST && rm $DST/$ZIP && cd $DST/FastQC && chmod 755 fastqc && ln -s $DST/FastQC/fastqc /usr/local/bin/fastqc

## Cutadapt v1.16

RUN pip install 'cutadapt==1.16'

## Trimgalore v0.4.5

WORKDIR /tmp/
RUN curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.tar.gz -o trim_galore.tar.gz
RUN tar xvzf trim_galore.tar.gz
RUN mv TrimGalore-0.4.5/trim_galore /usr/local/bin

## Bowtie2 v2.3.4.2

RUN curl -fsSL https://github.com/BenLangmead/bowtie2/releases/download/v2.3.4.2/bowtie2-2.3.4.2-linux-x86_64.zip -o bowtie2.zip
RUN unzip bowtie2.zip && rm bowtie2.zip
RUN mv bowtie2-2.3.4.2-linux-x86_64/ /usr/local/bin/bowtie2-2.3.4.2-linux-x86_64/
ENV PATH=${PATH}:/usr/local/bin/bowtie2-2.3.4.2-linux-x86_64/

## Samtools v1.9

RUN curl -fsSL https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 -o samtools.tar.bz2
RUN tar jxf samtools.tar.bz2
RUN cd samtools-1.9/ && ./configure && make && make install
WORKDIR /tmp/

## Bismark v0.19.1

RUN curl -fsSL https://github.com/FelixKrueger/Bismark/archive/0.19.1.zip -o bismark.zip
RUN unzip bismark.zip && rm bismark.zip
RUN mv Bismark-0.19.1/ /usr/local/bin/Bismark-0.19.1/
ENV PATH=${PATH}:/usr/local/bin/Bismark-0.19.1/

## Picard v2.18.11

RUN curl -fsSL https://github.com/broadinstitute/picard/releases/download/2.18.11/picard.jar -o picard.jar
RUN mv picard.jar /usr/local/bin/

RUN cd

################## END OF DOCKERFILE ######################