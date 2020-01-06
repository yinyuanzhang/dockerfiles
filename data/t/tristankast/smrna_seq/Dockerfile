FROM continuumio/miniconda
LABEL authors="Tristan Kast" \
      description="Docker image containing all requirements for nf-core/smrnaseq pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/smrnaseq/bin:$PATH

RUN conda install -c bioconda fastqc --override-channels
