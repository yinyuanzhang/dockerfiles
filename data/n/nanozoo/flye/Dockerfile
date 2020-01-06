FROM continuumio/miniconda3
ENV VERSION 2.5

RUN apt update && apt install -y procps && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN conda config --add channels conda-forge && \
		conda config --add channels bioconda && \
		conda config --add channels default

RUN conda install -y -c bioconda flye=$VERSION && conda clean -a
