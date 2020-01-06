# Bioconductor 3.9

FROM rocker/r-ver:3.6.0
MAINTAINER mike@steinbaugh.com

# Nuke cache dirs before installing packages.
RUN rm -f /var/lib/dpkg/available && rm -rf /var/cache/apt/*

# Install missing compilation dependencies.
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -qy \
        autoconf \
        automake \
        cargo \
        gtk-doc-tools \
        libbz2-dev \
        libcairo2-dev \
        libcurl4-openssl-dev \
        libfreetype6-dev \
        libgdal-dev \
        libglu1-mesa-dev \
        libharfbuzz-dev \
        liblzma-dev \
        libmagick++-dev \
        libmariadb-client-lgpl-dev \
        libpng-dev \
        libssh2-1-dev \
        libssl-dev \
        libtool \
        libudunits2-dev \
        libxml2-dev \
        libx11-dev \
        libz-dev \
        pkg-config \
        texlive \
        xorg

# Install R packages.
WORKDIR /tmp
ARG GITHUB_PAT
ADD install.R .
RUN R -f install.R
WORKDIR /
