FROM agrf/biocontainers_base:4.7.12

# METADATA
ARG GATK_VERSION=4.1.4.0

# ENV
ENV PATH=/opt/conda/bin:$PATH

# INSTALLATION
RUN conda install --channel bioconda --yes --freeze-installed \
    gatk4=${GATK_VERSION}

# Clean up image afterwards
RUN conda clean --all --force-pkgs-dirs --yes