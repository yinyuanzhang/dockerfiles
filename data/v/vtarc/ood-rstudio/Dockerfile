FROM rocker/verse:3.6.1

RUN install2.r rlecuyer ggplot2 doParallel Rcpp MASS RColorBrewer
## RUN ln -s ~/.Renviron_OOD_3.6.1 /usr/local/lib/R/etc/.Renviron
COPY auth /usr/lib/rstudio-server/bin/auth_helper
