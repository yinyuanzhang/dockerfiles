FROM rocker/rstudio

RUN apt-get update -qq && apt-get -y --no-install-recommends install \
  libxml2-dev \
  libcairo2-dev \
  libsqlite-dev \
  libmariadbd-dev \
  libmariadb-client-lgpl-dev \
  libpq-dev \
  libssh2-1-dev \
  libpoppler-cpp-dev \
  libwebp-dev \
  libjpeg-dev \
  libudunits2-dev \
  libgdal-dev \
  libxt-dev \
  && R -e "source('https://bioconductor.org/biocLite.R')" \
  && install2.r --error \
    --deps TRUE \
    shiny \
    shinydashboard \
    ddalpha \
    recipes \
    tidyverse \
    dplyr \
    ggplot2 \
    devtools \
    formatR \
    remotes \
    selectr \
    plyr \
    stringr \
    pdftools \
    reshape2 \
    RColorBrewer \
    scales \
    lubridate \
    RSQLite \
    plotly \
    dbplyr \
    readr \
    DT \
    data.table \
    readxl

## Notes: Above install2.r uses --deps TRUE to get Suggests dependencies as well,
## dplyr and ggplot are already part of tidyverse, but listed explicitly to get their (many) suggested dependencies.
## In addition to the the title 'tidyverse' packages, devtools is included for package development.
## RStudio wants formatR for rmarkdown, even though it's not suggested.
## remotes included for installation from heterogenous sources including git/svn, local, url, and specific cran versions