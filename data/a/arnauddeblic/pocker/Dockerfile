FROM docker.io/rocker/verse:3.6.0

USER 0

## Declaration of jemalloc in environment variables
ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libjemalloc.so.1

## Installation of phantomjs for non-html output formats
## (using install_phantomjs() function from webshot package, included in rocker/verse:3.6.0)
## Installation of jemalloc for memory optimisation
## Installation of R packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential chrpath libssl-dev libxft-dev \
    libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev \
    libssl-dev libjemalloc1 \ 
    && R -e 'webshot::install_phantomjs()' \
    && cp -p /root/bin/phantomjs /usr/lib/rstudio-server/bin/ \
    && install2.r --error --deps TRUE \
    rlist kableExtra rAmCharts flexdashboard plumber

USER 185
