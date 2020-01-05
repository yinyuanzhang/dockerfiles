FROM nfcore/base
LABEL authors="Marc Hoeppner" \
      description="Docker image containing all requirements for IKMB metagenomics pipeline"

COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/metagenomics-profiling-1.1/bin:/opt:$PATH
RUN apt-get -y install procps unzip
RUN cd opt && wget https://www.dropbox.com/sh/m4na8wefp53j8ej/AACU1-Nc0q2dUNRmc9pesUi4a/bin/bcftools && ln -s bcftools bcftools_0.1.19 && chmod +x bcftools
RUN /opt/conda/envs/metagenomics-profiling-1.1/bin/sample2markers.py -h
RUN cd /opt/conda/envs/metagenomics-profiling-1.1/bin && unlink bcftools
