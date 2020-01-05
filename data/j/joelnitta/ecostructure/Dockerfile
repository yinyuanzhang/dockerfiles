FROM rocker/geospatial:3.5.2

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
### R packages
# CRAN packages (dependencies of methClust and CountClust but for
# some reason don't get installed automatically)
&& install2.r -e slam \
  SQUAREM \
  boot \
# Bioconductor packages
&& Rscript -e 'source("http://bioconductor.org/biocLite.R")' \
  -e 'biocLite("Biobase")' \
# Github packages
&& Rscript -e 'devtools::install_github("kkdey/methClust")' \
  -e 'devtools::install_github("kkdey/CountClust")' \
  -e 'devtools::install_github("TaddyLab/maptpx")' \
  -e 'devtools::install_github("kkdey/ecostructure")'

WORKDIR /home/rstudio
