FROM rocker/shiny

RUN apt-get update && \
    apt-get install -y \
      libmariadb-client-lgpl-dev \
      libssl-dev \
      libxml2-dev

ADD packages.txt /

RUN R -e "install.packages(readLines('/packages.txt'), repos='https://cran.rstudio.com/')"
