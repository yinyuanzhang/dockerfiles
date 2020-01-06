FROM ubuntu:18.10

MAINTAINER Bio-Rad Support <support@bio-rad.com>

RUN apt-get update -y

RUN apt-get install -y samtools

# apt-get r-base has bug; update to R3.4.4 via cran
RUN apt-get update -y && \
	apt-get install -y tzdata && \
	apt-get install -y libcurl4-openssl-dev && \
	apt-get install -y libssl-dev && \
	apt-get install -y libxml2-dev && \
	apt-get install -y libgsl-dev && \
	apt-get install -y dirmngr && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu cosmic-cran35/" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y r-base


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN Rscript -e 'install.packages(c("readr", "ggplot2", "devtools","dplyr","data.table","cowplot"), repos = "http://cran.us.r-project.org"); devtools::install_github("caleblareau/BuenColors")'
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(c("GreenleafLab/chromVAR", "motifmatchr", "BiocParallel"))'

COPY src/* /

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/run_chromvar.sh"]
