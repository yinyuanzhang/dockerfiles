# Acid Genomics single-cell RNA-seq on Bioconductor 3.7

FROM acidgenomics/rnaseq:bioc-3.7
MAINTAINER mike@steinbaugh.com

ARG GITHUB_PAT

WORKDIR /tmp

RUN apt-get install -qy \
    python-pip python3-pip python3-venv && \
    python2.7 -m pip install --upgrade --user virtualenv

# Python 3 doesn't work quite right yet.
# > python3 -m venv ~/.virtualenvs/reticulate

ADD reticulate.R .
RUN R -f reticulate.R

ADD trapnell.R .
RUN R -f trapnell.R

ADD satija.R .
RUN R -f satija.R

ADD acidgenomics.R .
RUN R -f acidgenomics.R

WORKDIR /
