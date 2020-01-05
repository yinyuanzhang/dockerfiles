FROM rocker/r-base
MAINTAINER mark chang <ak0922747401@gmail.com>

RUN apt-get update -qq && apt-get install -y \
  git-core \
  libssl-dev \
  libcurl4-gnutls-dev

RUN R -e 'install.packages(c("devtools", "xts", "caret", "e1071", "curl", "magrittr", "stringr", "pacman"))' \
    && R -e 'devtools::install_github("trestletech/plumber")'

COPY . /inanalysisrserver

EXPOSE 8001
CMD cd  inanalysisrserver && Rscript serverStart.r