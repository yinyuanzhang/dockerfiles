## Emacs, make this -*- mode: sh; -*-

## Modified from rocker/hadleyverse

FROM rocker/drd

MAINTAINER "Francois Michonneau" francois.michonneau@gmail.com

RUN apt-get update \
    && apt-get install -t unstable -y --no-install-recommends \
	       aspell \
	       aspell-en \
	       ghostscript \
	       imagemagick \
	       lmodern \
	       pandoc \
	       pandoc-citeproc \
	       texlive-fonts-recommended \
	       texlive-humanities \
	       texlive-latex-extra \
	       texinfo \
    && apt-get clean \
    #&& cd /usr/share/texlive/texmf-dist \
    #&& wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \
    #&& unzip inconsolata.tds.zip \
    #&& rm inconsolata.tds.zip \
    #&& echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \
    && mktexlsr \
    && updmap-sys

## Install some external dependencies.
RUN apt-get update \
    && apt-get install -y --no-install-recommends -t unstable \
	       default-jdk \
	       default-jre \
	       gdal-bin \
	       icedtea-netx \
	       libatlas-base-dev \
	       libcairo2-dev \
	       libgsl0-dev \
	       libgdal-dev \
	       libgeos-dev \
	       libgeos-c1v5 \
	       libpoppler-cpp-dev \
	       librdf0-dev \
	       libssl-dev \
	       libpq-dev \
	       libgit2-dev \
	       libsqlite3-dev \
	       libv8-dev \
	       libxcb1-dev \
	       libxdmcp-dev \
	       libxml2-dev \
	       libxslt1-dev \
	       libxt-dev \
	       netcdf-bin \
	       qpdf \
	       r-cran-rgl \
	       ssh \
	       vim \
    && R CMD javareconf \
    && RD CMD javareconf


## Install needed dependencies
RUN RD -e 'update.packages(ask=FALSE, checkBuilt=TRUE); install.packages(c("devtools", "remotes", "git2r", "knitr", "rmarkdown", "testthat", "xml2", "ade4", "ape", "aRxiv", "assertthat", "bibtex", "bitops", "bold", "brew", "caTools", "chron", "coda", "codetools", "colorspace", "corpcor", "crayon", "cubature", "data.table", "DBI", "devtools", "evaluate", "dichromat", "dplyr", "foreach", "formatR", "fulltext", "ggplot2", "gdata", "git2r", "gtable", "highr", "htmltools", "iterators", "jsonlite", "labeling", "lattice", "lubridate", "markdown", "MCMCglmm", "memoise", "munsell", "nlme", "NLP", "nnet", "phylobase", "plyr", "praise", "R.cache", "R.methodsS3", "R.oo", "R.utils", "R6", "RColorBrewer", "Rcpp", "readxl", "rentrez", "reshape", "reshape2", "rex", "rjson", "rmarkdown", "RNeXML", "rncl", "roxygen2", "rotl", "rplos", "rredis", "rstudioapi", "rversions", "scales", "slam", "solr", "survival", "taxize", "tensorA", "tidyr", "tidyverse", "tm", "uuid", "XML", "yaml"), repos=c(CRAN = "http://cloud.r-project.org", bioc="http://www.bioconductor.org/packages/release/bioc"))'

## httr authentication uses this port
EXPOSE 1410
ENV HTTR_LOCALHOST 0.0.00.
