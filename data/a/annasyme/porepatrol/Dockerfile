
FROM nfcore/base
LABEL authors="Anna Syme" \
      description="Docker image containing all requirements for nf-core/porepatrol pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/nf-core-porepatrol-1.0dev/bin:$PATH


