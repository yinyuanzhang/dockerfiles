FROM rocker/rstudio

MAINTAINER "Christoph Burow" christoph.burow@gmx.net

RUN apt-get update -qq \
	&& apt-get -y --no-install-recommends install \
		libxt-dev \
		libcairo2-dev \
		libxml2-dev \
		libx11-dev \
		libcgal-dev \
		libglu1-mesa-dev \
		libmagick++-dev \
		libhunspell-dev \
		libgeos-dev \
		libudunits2-dev \
		libgdal-dev \
		libgit2-dev \
## Build JAGS-4 from source (debian:stable is still on JAGS-3.x.y)
	&& wget https://sourceforge.net/projects/mcmc-jags/files/JAGS/4.x/Source/JAGS-4.3.0.tar.gz -O jags.tar.gz \
	&& tar -xf jags.tar.gz \
    && cd JAGS* && ./configure && make && make install \
    && cd / && rm -rf jags.tar.gz JAGS* 

## Use Debian unstable to install binary r packages, mainly
## to save time on Travis CI
RUN echo "deb http://http.debian.net/debian sid main" > /etc/apt/sources.list.d/debian-unstable.list

RUN apt-get update -qq \
	&& apt-get -t unstable -y --no-install-recommends install \
		r-cran-rcpp \
		r-cran-rcppeigen \
		r-cran-bbmle \
		r-cran-testthat \
		r-cran-sp \
		r-cran-raster \
		r-cran-rmarkdown \
		r-cran-ggplot2 \
		r-cran-devtools \
		r-cran-tidyverse \
		r-cran-rgl \
		r-cran-interp

## Let R know about the package site and set default download method
## For the latter see https://stackoverflow.com/questions/36803908/trouble-installing-packages-in-centos-internet-routines-cannot-be-loaded/36874346
RUN export R_LIBS_SITE="/usr/lib/R/site-library/" \
	&& echo 'options("download.file.method" = "wget")' > ~/.Rprofile 