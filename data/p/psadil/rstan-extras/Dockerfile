FROM jrnold/rstan:latest
MAINTAINER Patrick Sadil psadil@gmail.com

RUN apt-get update -qq && apt-get -y --no-install-recommends install \
    libzmq3-dev \
    libudunits2-dev

RUN install2.r --error \
    BiocManager
RUN Rscript -e 'BiocManager::install("CodeDepends")'

# Install 'extras'
RUN install2.r --error \
    drake \
    brms \
    tidybayes
