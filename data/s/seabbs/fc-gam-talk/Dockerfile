FROM rocker/tidyverse

RUN apt-get install -y \
    texlive-latex-recommended \
    texlive-fonts-extra \
    texinfo \
    libqpdf-dev \
    mesa-common-dev \
    libglu1-mesa-dev \
    && apt-get clean
    
ADD . /home/rstudio/gam-uob-course

WORKDIR /home/rstudio/gam-uob-course

RUN Rscript gams-setup.R

## Get github packages
RUN Rscript -e 'devtools::install_github('yihui/xaringan')`