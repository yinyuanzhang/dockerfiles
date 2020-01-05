FROM kaixhin/cuda-mxnet:8.0

RUN sudo apt-get update

# install EBImage
RUN sudo apt-get install -y libfftw3-dev
RUN Rscript -e "source('https://bioconductor.org/biocLite.R'); biocLite('EBImage')"

# install mxnet for R
RUN apt-get -y build-dep libcurl4-gnutls-dev
RUN apt-get -y install libcurl4-gnutls-dev
RUN Rscript -e "install.packages('devtools', repo = 'https://cran.rstudio.com')"
RUN cd /root/mxnet/R-package && Rscript -e "library(devtools); library(methods); options(repos=c(CRAN='https://cran.rstudio.com')); install_deps(dependencies = TRUE)" && cd .. && make rpkg && R CMD INSTALL mxnet_0.7.tar.gz
RUN ln /dev/null /dev/raw1394

#cleanup
RUN rm -rf /var/lib/apt/lists/*
