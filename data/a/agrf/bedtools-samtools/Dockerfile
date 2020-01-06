FROM agrf/biocontainers_base:4.7.12

# METADATA
ARG SAMTOOLS_VERSION=1.9
ARG BEDTOOLS_VERSION=2.28.0

# ENV
ENV PATH=/opt/conda/bin:$PATH

# INSTALLATION
RUN conda install --channel bioconda --yes --freeze-installed \
    samtools=${SAMTOOLS_VERSION} bedtools=${BEDTOOLS_VERSION}

# Clean up image afterwards
RUN conda clean --all --force-pkgs-dirs --yes