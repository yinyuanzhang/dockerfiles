####### Dockerfile #######
FROM rocker/verse:latest
# verse gives all rmarkdown-related stuff including TinyTeX, as well as tidyverse.

MAINTAINER Tom Wallis (thomas.wallis@uni-tuebingen.de)

# ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND=noninteractive

# Set the time zone correctly
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install SSH, etc.
RUN apt-get update -qq && apt-get install -yq -qq --no-install-recommends \
    openssh-server \
    screen \
    tmux \
    build-essential \
    libgsl-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# hardwire RStudio theme
RUN echo "uiPrefs={\"theme\" : \"Solarized Dark\"}" >> \
  /home/rstudio/.rstudio/monitored/user-settings/user-settings

RUN install2.r --error \
    --deps TRUE \
    devtools

RUN R --no-restore \
    --no-save -e \
    'devtools::install_github("crsh/papaja")'

RUN install2.r --error \
    --deps TRUE \
    ggthemes \
    gridExtra \
    here \
    gsl \
    psyphy \
    RWiener \
    rtdists \
    ez \
    schoRsch \
    foreach \
    emmeans \
    ggridges \
    ggbeeswarm

RUN install2.r --error \
    tidybayes

# install dev version of brms for bug fix:
RUN R --no-restore \
    --no-save -e \
    'devtools::install_github("paul-buerkner/brms", ref = "fb32bf5")'
