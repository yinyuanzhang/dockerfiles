# basejump on Bioconductor 3.7

FROM acidgenomics/bioconductor:3.7
MAINTAINER mike@steinbaugh.com

# Install R packages.
WORKDIR /tmp
ARG GITHUB_PAT
ADD install.R .
RUN R -f install.R
WORKDIR /
