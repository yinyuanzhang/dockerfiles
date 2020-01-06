FROM nfcore/base
LABEL description="Docker image containing all requirements for czbiohub/nf-large-assembly pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/nf-large-assembly-1.0dev/bin:$PATH
