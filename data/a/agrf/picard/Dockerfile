FROM agrf/biocontainers_base:4.7.12

# METADATA
ARG PICARD_VERSION=2.18.27
ARG R_VERSION=3.5.1

# ENV
ENV PATH=/opt/conda/bin:$PATH

# INSTALLATION
RUN conda install --channel bioconda --yes --freeze-installed \
    picard=${PICARD_VERSION}

# R is also required for some of the metric files
RUN conda install --channel r --yes --freeze-installed \
    r-essentials=3.6.0 \
    r-base=3.6.0 \
    r-cairo=1.5_10

# Clean up image afterwards
RUN conda clean --all --force-pkgs-dirs --yes

# Set R environment variables for runtime
ENV R_HOME=/opt/conda/lib/R
# Thess makes Rscript basically use '--vanilla'
# https://stat.ethz.ch/R-manual/R-devel/library/base/html/Startup.html
ENV R_ENVIRON_USER=""
ENV R_PROFILE_USER=""

