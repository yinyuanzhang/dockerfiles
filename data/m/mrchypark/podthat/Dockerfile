FROM rocker/r-ver:3.6.1

RUN apt-get update && apt-get install -y libcurl4-openssl-dev libxml2-dev libssl-dev zlib1g-dev libpcre3-dev liblzma-dev libbz2-dev

RUN Rscript -e "install.packages(c('littler','pak'))"

COPY install.R /install.R

RUN r install.R
