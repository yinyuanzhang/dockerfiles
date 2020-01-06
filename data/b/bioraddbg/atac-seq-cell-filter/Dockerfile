FROM ubuntu:18.10

MAINTAINER Bio-Rad Support <support@bio-rad.com>

RUN apt-get update && \
	apt-get install -y tzdata && \
	apt-get install -y python-pip && \
	apt-get install -y dirmngr && \
	apt-get install -y libcurl4-openssl-dev && \
	apt-get install -y libssl-dev && \
	pip install numpy && \
	pip install scipy && \
	pip install pysam && \
	pip install pandas

RUN apt-get install -y python3 && \
    apt-get install -y python3-dev && \
    apt-get install -y libcurl4-openssl-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y python3-venv && \
    apt-get install -y samtools

RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu cosmic-cran35/" >> /etc/apt/sources.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

RUN apt-get update && \
	apt-get install -y r-base

RUN Rscript -e 'install.packages(c("dplyr","ggplot2","cowplot"), repos = "http://cran.us.r-project.org")'

RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(c("GenomicAlignments", "Rsamtools", "BiocParallel"))'

ADD src/kneeCaller.py /src/kneeCaller.py

ADD src/pyDensityCalc.R /src/pyDensityCalc.R

ADD src/dropBarcodeUniqueCounts.R /src/dropBarcodeUniqueCounts.R

ADD src/beadsPerDrop.R /src/beadsPerDrop.R

ADD src/split_count_species.py /src/split_count_species.py

ADD src/plotCrosstalk.R /src/plotCrosstalk.R

ADD src/callKnee.sh /src/callKnee.sh

ADD src/tagBamFile.py /src/tagBamFile.py

COPY bedtools/ /bedtools/

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/src/callKnee.sh"]
