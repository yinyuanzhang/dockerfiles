FROM nfcore/base
LABEL authors="Anna Syme" \
      description="Docker image containing all requirements for nf-core/plantgenome pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/nf-core-plantgenome-1.0dev/bin:$PATH
