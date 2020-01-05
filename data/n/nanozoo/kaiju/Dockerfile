FROM continuumio/miniconda3
ENV VERSION 1.7.2 

RUN apt update && apt install -y procps && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda config --add channels default

RUN conda install kaiju=$VERSION && conda clean -a
#ready-to-use dbs can be found here: http://kaiju.binf.ku.dk/server