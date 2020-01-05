FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

# Install.
RUN \
  apt-get update && \
  apt-get -y dist-upgrade && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:opencpu/opencpu-2.0 && \
  apt-get update && \
  apt-get install -y opencpu-server

# Prints apache logs to stdout
RUN \
  ln -sf /proc/self/fd/1 /var/log/apache2/access.log && \
  ln -sf /proc/self/fd/1 /var/log/apache2/error.log && \
  ln -sf /proc/self/fd/1 /var/log/opencpu/apache_access.log && \
  ln -sf /proc/self/fd/1 /var/log/opencpu/apache_error.log

# Apache ports
EXPOSE 80
EXPOSE 443
EXPOSE 8004

## LinenStats Stuff

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    ed \
    less \
    locales \
    wget \
    ca-certificates \
    git \
    # Document generation
    fonts-texgyre \
    texlive-full \
    # Image Library
    libcairo2-dev \
    # Postgres Library
    libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/ \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# Install Pandoc
RUN wget https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb \
  && dpkg -i pandoc*.deb

# Setup for Shiny Proxy ----------
# Force Shiny to use 3838 and allow connections from all hosts
# Also configure the default CRAN repo
COPY Rprofile.site /usr/lib/R/etc/

# Install devtools so version numbers can be specified
RUN R -e "install.packages(c('devtools'))"

# # Install R package dependencies
RUN R -e "devtools::install_version('R6', version = '2.2.2')" \
      -e "devtools::install_version('magrittr', version = '1.5')" \
      -e "devtools::install_version('assertthat', version = '0.2.0')" \
      -e "devtools::install_version('prettyunits', version = '1.0.2')" \
      -e "devtools::install_version('blob', version = '1.1.1')" \
      -e "devtools::install_version('mnormt', version = '1.5-5')" \
      -e "devtools::install_version('psych', version = '1.8.4')" \
      # C++
      -e "devtools::install_version('Rcpp', version = '0.12.17')" \
      -e "devtools::install_version('BH', version = '1.66.0-1')" \
      -e "devtools::install_version('plogr', version = '0.2.0')" \
      # Strings, Parsing, & Formatting
      -e "devtools::install_version('yaml', version = '2.1.19')" \
      -e "devtools::install_version('stringi', version = '1.2.3')" \
      -e "devtools::install_version('pillar', version = '1.2.2')" \
      -e "devtools::install_version('glue', version = '1.2.0')" \
      # Database Access
      -e "devtools::install_version('DBI', version = '1.0.0')" \
      -e "devtools::install_version('RPostgreSQL', version = '0.6-2')" \
      -e "devtools::install_version('RPostgres', version = '1.1.0')" \
      # Package Development
      -e "devtools::install_version('pkgconfig', version = '2.0.1')" \
      # Tidyverse
      -e "devtools::install_version('rlang', version = '0.2.1')" \
      -e "devtools::install_version('tibble', version = '1.4.2')" \
      -e "devtools::install_version('purrr', version = '0.2.5')" \
      -e "devtools::install_version('tidyselect', version = '0.2.4')" \
      -e "devtools::install_version('dplyr', version = '0.7.6')" \
      -e "devtools::install_version('dbplyr', version = '1.2.1')" \
      -e "devtools::install_version('stringr', version = '1.3.1')" \
      -e "devtools::install_version('broom', version = '0.4.4')" \
      -e "devtools::install_version('lubridate', version = '1.7.4')" \
      -e "devtools::install_version('tidyr', version = '0.8.1')" \
      -e "devtools::install_version('forcats', version = '0.2.0')" \
      -e "devtools::install_version('hms', version = '0.4.2')" \
      # Other useful packages
      -e "devtools::install_version('wrapr', version = '1.4.0')" \
      # Plots
      -e "devtools::install_version('ggplot2', version = '2.2.1')" \
      -e "devtools::install_version('ggridges', version = '0.5.0')" \
      # Assertions
      -e "devtools::install_version('checkmate', version = '1.8.5')" \
      -e "devtools::install_version('assertive.base', version='0.0-7')" \
      -e "devtools::install_version('assertive.types', version='0.0-3')" \
      -e "devtools::install_version('assertive.properties', version='0.0-4')" \
      -e "devtools::install_version('assertive.strings', version='0.0-3')" \
      # Testing Packages
      -e "devtools::install_version('withr', version = '2.1.2')" \
      -e "devtools::install_version('testthat', version = '2.0.0')" \
      -e "devtools::install_version('covr', version = '3.0.1')" \
      -e "devtools::install_version('lintr', version = '1.0.2')" \
      -e "devtools::install_version('mockery', version = '0.4.1')" \
      -e "devtools::install_version('rprojroot', version = '1.3-2')" \
      # Documentation
      -e "devtools::install_version('tinytex', version = '0.5')" \
      -e "devtools::install_version('commonmark', version = '1.4')" \
      -e "devtools::install_version('rmarkdown', version = '1.9')" \
      -e "devtools::install_version('roxygen2', version = '6.0.1')" \
      # Document Generation
      -e "devtools::install_version('knitr', version = '1.20')" \
      -e "devtools::install_version('printr', version = '0.1')" \
      # Shiny Dependencies
      -e "devtools::install_version('later', version = '0.7.3')" \
      -e "devtools::install_version('httpuv', version = '1.4.4.1')" \
      # Shiny
      -e "devtools::install_version('shiny', version = '1.1.0')" \
      -e "devtools::install_version('htmlwidgets', version = '1.2')" \
      -e "devtools::install_version('plotly', version = '4.7.1')" \
      -e "devtools::install_version('rbokeh', version = '0.5.0')" \
      -e "devtools::install_version('shinydashboard', version = '0.7.0')" \
      -e "devtools::install_version('formattable', version = '0.2.0.1')" \
      -e "devtools::install_version('DT', version = '0.4')" \
      -e "devtools::install_version('shinyjs', version = '1.0')" \
      # Prediction Dependencies
      -e "devtools::install_version('zoo', version = '1.8-2')" \
      -e "devtools::install_version('xts', version = '0.10-2')" \
      -e "devtools::install_version('dygraphs', version = '1.1.1.5')" \
      -e "devtools::install_version('extraDistr', version = '1.8.9')" \
      -e "devtools::install_version('gridExtra', version = '2.3')" \
      -e "devtools::install_version('rstan', version = '2.17.3')" \
      -e "devtools::install_version('inline', version = '0.3.15')" \
      -e "devtools::install_version('RcppEigen', version = '0.3.3.4.0')" \
      -e "devtools::install_version('StanHeaders', version = '2.17.2')" \
      -e "devtools::install_version('StanHeaders', version = '2.17.2')" \
      # Prediction
      -e "devtools::install_version('prophet', version = '0.3.0.1')"


EXPOSE 3838

# Start non-daemonized webserver
CMD apachectl -DFOREGROUND
