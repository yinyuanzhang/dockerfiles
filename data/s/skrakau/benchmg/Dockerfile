FROM nfcore/base
LABEL authors="Sabrina Krakau" \
      description="Docker image containing all requirements for nf-core/benchmg pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/nf-core-benchmg-1.0dev/bin:$PATH
