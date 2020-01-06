FROM continuumio/miniconda3
ENV VERSION 1.11

RUN apt update && apt-get -y install libncurses5 && apt-get clean

RUN conda install conda=4.6

RUN conda config --add channels bioconda && conda config --add channels conda-forge

RUN conda install detonate=$VERSION bowtie=1.2.3 blat=36 samtools=1.3
