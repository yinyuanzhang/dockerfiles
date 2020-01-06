FROM rocker/shiny-verse:3.5.3

RUN apt-get update -qq --fix-missing && \
  apt-get -y --no-install-recommends install \
    libv8-dev \
    libudunits2-dev \
    libgdal-dev \
    libgeos-dev \
    libproj-dev

RUN R -e "source('https://bioconductor.org/biocLite.R')" \
  && install2.r --error \
    --deps TRUE \
    pacman \
    dplyr \
    shinyjs \
    shinyBS \
    readxl \
    plotly \
    DT \        
    markdown \
    randomForest \
    glmnet \
    argonR \
    argonDash \
    magrittr

RUN rm -rf /tmp/downloaded_packages/ /tmp/*.rds