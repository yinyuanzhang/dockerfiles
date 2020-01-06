FROM python:2.7

MAINTAINER Bio-Rad Support <support@bio-rad.com>

RUN pip install numpy && pip install MACS2

RUN apt-get update && apt-get install -y r-base

RUN Rscript -e 'install.packages(c("data.table", "argparse"), repos = "http://cran.us.r-project.org")'

RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite("GenomicRanges")'

COPY src/callPeaks.sh /callPeaks.sh

COPY src/summitsToCleanPeaks.R /summitsToCleanPeaks.R

COPY bedtools/ /bedtools/

COPY blacklist/ /blacklist/

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/callPeaks.sh"]
