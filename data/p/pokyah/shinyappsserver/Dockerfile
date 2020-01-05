FROM r-base:latest

MAINTAINER Thomas Goossens "hello.pokyah@gmail.com"

## Install dependencies and Download and install shiny server

## See https://www.rstudio.com/products/shiny/download-server/ for the
## instructions followed here.

RUN apt-get update && apt-get install -y -t unstable \
    sudo \
    libudunits2-dev \
    units \
    libxt-dev \
    libssl-dev \
    libxml2 \
    libxml2-dev \
    gdal-bin \
    libgdal-dev \
    gdebi-core \
    pandoc \
    pandoc-citeproc \
    libcurl4-gnutls-dev \
    libcairo2-dev/unstable \
    libxt-dev && \
    wget --no-verbose https://download3.rstudio.org/ubuntu-14.04/x86_64/VERSION -O "version.txt" && \
    VERSION=$(cat version.txt)  && \
    wget --no-verbose "https://download3.rstudio.org/ubuntu-14.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
    gdebi -n ss-latest.deb && \
    rm -f version.txt ss-latest.deb && \
    R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')" && \
    cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 3838

COPY shiny-server.sh /usr/bin/shiny-server.sh

## Uncomment the line below to include a custom configuration file. You can download the default file at
## https://raw.githubusercontent.com/rstudio/shiny-server/master/config/default.config
## (The line below assumes that you have downloaded the file above to ./shiny-customized.config)
## Documentation on configuration options is available at
## http://docs.rstudio.com/shiny-server/

# COPY shiny-customized.config /etc/shiny-server/shiny-server.conf

# RUN R -e "install.packages(c('Rcpp', 'devtools', 'shiny', 'rmarkdown'), repos='http://cran.rstudio.com/')"

RUN su - -c "R -e \"install.packages(c('Rcpp', 'devtools', 'shiny', 'rmarkdown'), repos='http://cran.rstudio.com/')\""

RUN su - -c "R -e \"devtools::install_github('pokyah/defHydWal', ref='dockerized', force=TRUE)\""

# RUN su - -c "R -e \"devtools::install_github('pokyah/defHydWal', ref='dockerized', force=TRUE)\"" &  chown -R shiny:shiny /usr/local/lib/R/site-library/defHydWal/ & systemctl restart shiny-server

CMD ["/usr/bin/shiny-server.sh"]
