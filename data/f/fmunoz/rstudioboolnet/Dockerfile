FROM rocker/rstudio:3.4.4
MAINTAINER "Felipe de Jesus Muñoz Gonzalez" fmunoz@lcg.unam.mx

RUN  apt-get -y -q dist-upgrade 

#RUN apt-get -y update -qq  && apt-get -y upgrade

#RUN apt-get install -y --no-install-recommends apt-utils  software-properties-common 

#RUN  add-apt-repository -y ppa:ubuntu-toolchain-r/test 

RUN  apt-get -y update -qq  && sudo apt-get -y upgrade

RUN  apt-get install -y --no-install-recommends libpangoft2-1.0-0  \
    libxt-dev \
    xvfb \
    xauth \ 
    xfonts-base \
    libglib2.0-0  \
    libglib2.0-bin  \
    libglib2.0-dev \
    libpango-1.0-0  \
    libxml2-dev \
    libsqlite3-dev \
    libmariadbd-dev \
    libmariadb-client-lgpl-dev \
    libgdk-pixbuf2.0-dev \
    libatk1.0-dev \
    libssl1.0.0  \
    libpangocairo-1.0-0 \
    libcairo2  \
    libpq-dev \
    libcairo2-dev \ 
    fonts-dejavu \
    gfortran \
    libssh2-1-dev \
    unixodbc-dev \
    r-cran-xml \
    r-cran-plyr \ 
    r-cran-ggplot2 \
    r-cran-gplots \
    r-cran-boolnet  \ 
    libnlopt-dev \
    xml-core \
    lsb-release \
    libssl-dev \
    gcc && apt-get clean
    
RUN  Rscript -e "install.packages('devtools',lib='/usr/local/lib/R/site-library',dependencies=T)"
RUN  Rscript -e "library(devtools); install_github('mar-esther23/boolnet-perturb')"
RUN  Rscript -e "install.packages('devtools',lib='/usr/local/lib/R/site-library',dependencies=T)"
RUN  Rscript -e "install.packages(c('tidyverse','dplyr','formatR'),lib='/usr/local/lib/R/site-library',dependencies=T)"
RUN  Rscript -e "install.packages(c('remotes','selectr','caTools','biocManager'),lib='/usr/local/lib/R/site-library',dependencies=T)"
RUN  Rscript -e "install.packages(c('igraph','dendextend','dendextendRcpp'),lib='/usr/local/lib/R/site-library',dependencies=T)"

