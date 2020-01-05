FROM continuumio/miniconda3
ENV VERSION 0.9.1 

RUN useradd --create-home nanozoo
WORKDIR /home/nanozoo

RUN conda config --add channels conda-forge && \
    conda config --add channels bioconda && \
    conda config --add channels default

RUN conda install multiqc=$VERSION && conda clean -a

USER nanozoo