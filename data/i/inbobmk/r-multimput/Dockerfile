FROM r-base

MAINTAINER "Thierry Onkelinx" thierry.onkelinx@inbo.be

## docker build -t inbobmk/r-multimput .

## Install wget
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    wget \
  && apt-get clean

## install devtools
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    git \
    libssl-dev \
    libssh2-1-dev \
  && Rscript -e 'install.packages("devtools")' \
  && apt-get clean

## install assertthat
RUN Rscript -e 'install.packages("assertthat")'

## install covr
RUN Rscript -e 'install.packages("covr")'

## install dplyr
RUN Rscript -e 'devtools::install_github("hadley/dplyr")'

## install INLA
RUN Rscript -e 'install.packages("sp")' \
  && Rscript -e 'install.packages("INLA", repos="http://www.math.ntnu.no/inla/R/stable")'

## install knitr
RUN Rscript -e 'install.packages("knitr")'

## install lintr
RUN Rscript -e 'install.packages("lintr")'

## install lme4
RUN Rscript -e 'install.packages("lme4")'

## install mgcv
RUN Rscript -e 'install.packages("mgcv")'

## install mvtnorm
RUN Rscript -e 'install.packages("mvtnorm")'

## Install rmarkdown
RUN wget https://github.com/jgm/pandoc/releases/download/1.16.0.2/pandoc-1.16.0.2-1-amd64.deb \
  && dpkg -i pandoc-1.16.0.2-1-amd64.deb \
  && rm pandoc-1.16.0.2-1-amd64.deb \
  && Rscript -e 'install.packages("rmarkdown")'

## install snowfall
RUN Rscript -e 'install.packages("snowfall")'

## install tidyr
RUN Rscript -e 'install.packages("tidyr")'

## Add minimal LaTeX configuration
## Taken from https://github.com/rocker-org/hadleyverse/blob/master/Dockerfile
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    lmodern \
    texlive-fonts-recommended \
    texlive-humanities \
    texlive-latex-extra \
    texinfo \
  && apt-get clean \
  && cd /usr/share/texlive/texmf-dist \
  && wget http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \
  && unzip inconsolata.tds.zip \
  && rm inconsolata.tds.zip \
  && echo "Map zi4.map" >> /usr/share/texlive/texmf-dist/web2c/updmap.cfg \
  && mktexlsr \
  && updmap-sys
