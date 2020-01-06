FROM rocker/tidyverse:latest

# System requirements
RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  build-essential \
  curl \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

# R packages
RUN R -e "source('https://bioconductor.org/biocLite.R')" \
  && install2.r --error --deps TRUE \
    feather \
    gTests \
    magrittr \
    MixSim \
    mixtools \
    mvnTest \
    parallelDist \
    vegan

# Python dependencies
RUN pip3 install --upgrade pip setuptools
RUN pip3 install \
  bokeh \
  feather-format \
  fire \
  numpy \
  pandas \
  scipy \
  scikit-learn
