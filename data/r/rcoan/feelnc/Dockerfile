############################################################
# Dockerfile to build FEELnc, a tool to find lncRNA
# Includes all dependencies
# Please send an e-mail for improovements in the Dockerfile
# FEELnc GitHub: https://github.com/tderrien/FEELnc
############################################################

FROM ubuntu:16.04

LABEL maintainer="Rafael Coan (rafael.coan@unesp.br)" \
      description="FEELnc lncRNA classifier." \
      version="0.1.1"

# install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    perl \
    bioperl \
    r-base

# install Parallel::ForkManager
RUN cpan Parallel::ForkManager

# install R packages
WORKDIR /docker
RUN wget -cq "https://cran.r-project.org/src/contrib/randomForest_4.6-14.tar.gz" && \
    R -e "install.packages('ROCR', dependencies=TRUE, repos='http://cran.rstudio.com/')" && \
    R CMD INSTALL -c randomForest_4.6-14.tar.gz

# install FEELnc
WORKDIR /docker
RUN wget -cq "https://codeload.github.com/tderrien/FEELnc/zip/master" -O FEELnc-master.zip && \
    unzip FEELnc-master.zip

ENV FEELNCPATH="/docker/FEELnc-master"
ENV PERL5LIB=$PERL5LIB:${FEELNCPATH}/lib/
ENV PATH=$PATH:${FEELNCPATH}/scripts/
ENV PATH=$PATH:${FEELNCPATH}/utils/
ENV PATH=$PATH:${FEELNCPATH}/bin/LINUX/

# clean
RUN rm -rf /docker/FEELnc-master.zip && \
    rm -rf /docker/randomForest_4.6-14.tar.gz && \
    apt-get clean && \
    apt-get remove --yes --purge wget
