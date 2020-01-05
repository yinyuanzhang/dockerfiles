FROM ubuntu:18.10
RUN apt-get update && apt-get install -y tzdata && apt-get install -y git
RUN git clone https://895978976479a9979702704923ed384c0c6c4713@github.com/caleblareau/bap.git /bap

MAINTAINER Bio-Rad Support <support@bio-rad.com>

RUN apt-get update -y && \
	apt-get install -y python3 && \
	apt-get install -y python3-dev && \
	apt-get install -y libcurl4-openssl-dev && \
	apt-get install -y libssl-dev && \
	apt-get install -y dirmngr && \
	apt-get install -y samtools && \
	apt-get install -y python3-venv && \
	apt-get install -y parallel && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu cosmic-cran35/" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y r-base

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN Rscript -e 'install.packages(c("devtools","dplyr","data.table","cowplot"), repos = "http://cran.us.r-project.org"); devtools::install_github("caleblareau/BuenColors")'

RUN Rscript -e 'source("https://bioconductor.org/biocLite.R"); biocLite(c("GenomicAlignments", "SummarizedExperiment", "GenomicRanges", "BiocParallel", "Rsamtools"))'

RUN Rscript -e 'devtools::install_github("digitalbiology/kneecallr", auth_token=as.character("895978976479a9979702704923ed384c0c6c4713"))'

RUN Rscript -e 'install.packages(c("argparse","doParallel","foreach"))'

##################
# Create Bap Env #
##################
RUN python3 -m venv /br_tools/bap_venv 
RUN /br_tools/bap_venv/bin/pip install pysam #this is timing out when done as part of the bap install...
RUN /br_tools/bap_venv/bin/pip install /bap/
RUN apt-get install -y python-pip
RUN python2.7 -m pip install numpy scipy

COPY src/callBeadKnee.R /callBeadKnee.R

COPY src/callJaccardKnee.R /callJaccardKnee.R

COPY src/filterBeads.sh /filterBeads.sh

COPY src/getImplicatedBarcodes.R /getImplicatedBarcodes.R

COPY src/quantNuclearFrags.py /quantNuclearFrags.py

COPY src/bamCounter.R /bamCounter.R

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/filterBeads.sh"]
