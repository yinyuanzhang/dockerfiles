FROM continuumio/miniconda3:latest
MAINTAINER CHEN,Yuelong <yuelong.chen.btr@gmail.com>

ARG conda_forge='python=3.7.3 libopenblas libiconv'
ARG r='r'
ARG bioconda='bioconductor-affy java-jdk \
    bioconductor-annotate bioconductor-org.Hs.eg.db bioconductor-sva bioconductor-limma \
    r-pamr bioconductor-bladderbatch'
ARG greenelab='hgu133plus2hsentrezgcdf '


USER root
ENV PATH /opt/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:$PATH
RUN echo $PATH \
    && conda install -y -c r $r \
    && conda install -y -c conda-forge $conda_forge \
    && conda install -y -c bioconda $bioconda \
    && conda install -y -c greenelab $greenelab

RUN pip install git+https://github.com/btrspg/bioplots.git

RUN mkdir -p /opt/bin /opt/database
COPY DockerEnv/database/ /opt/database
COPY DockerEnv/CIBERSORT /opt/bin/
COPY rscripts/* /opt/bin/
COPY shscripts/* /opt/bin/


CMD bash





