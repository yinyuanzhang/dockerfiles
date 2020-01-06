# get the base image, the rocker/verse has R, RStudio and pandoc
FROM rocker/verse:3.5.3

# required
MAINTAINER Frederick Boehm <frederick.boehm@gmail.com>

COPY . /home/rstudio/hotspots

# go into the repo directory
RUN . /etc/environment \
  \
  # Install linux depedendencies here
  # e.g. need this for ggforce::geom_sina
  && sudo apt-get update \
  && sudo apt-get install libudunits2-dev -y \
  # build this compendium package
  && cd /home/rstudio/hotspots; make
