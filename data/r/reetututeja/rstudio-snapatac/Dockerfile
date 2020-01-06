FROM cyversevice/rstudio-base:latest
RUN apt-get update
RUN apt-get install -y tzdata libxml2-dev libpng-dev libssl-dev libcurl4-openssl-dev
#RUN apt-get install -y libopenblas-base

RUN Rscript -e 'install.packages(c("xml2","roxygen2","rversions","devtools"));'
RUN Rscript -e 'install.packages(c("doSNOW","Matrix"));'
RUN Rscript -e 'install.packages(("plot3D"));'
RUN Rscript -e 'devtools::install_github("r3fang/SnapATAC")'

RUN ["chmod", "+x", "/usr/local/bin/run.sh"]
