FROM ubuntu:16.04

MAINTAINER Bio-Rad Support <support@bio-rad.com>

ENV BWA_VERSION 0.7.17

RUN apt-get update && apt-get install -y \
  curl \
  bzip2 \
  make \
  gcc \
  zlib1g-dev \
	libncurses5-dev \
	wget \
	python-pip


RUN pip install --upgrade pip==9.0.3 && pip install pysam

RUN curl -SLO http://downloads.sourceforge.net/project/bio-bwa/bwa-${BWA_VERSION}.tar.bz2 && tar -xvjf bwa-${BWA_VERSION}.tar.bz2 && rm bwa-${BWA_VERSION}.tar.bz2 && cd /bwa-${BWA_VERSION} && make

RUN wget "https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2"  && tar xfj samtools-1.9.tar.bz2  && (cd samtools-1.9 && ./configure --disable-bz2 --disable-lzma && make) && rm /samtools-1.9.tar.bz2

COPY src/runBwa.sh /runBwa.sh

COPY src/tagBamFile.py /tagBamFile.py

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/runBwa.sh"]
