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
  python-pip \
  libbz2-dev \
  liblzma-dev \
  openjdk-8-jre-headless

# Install Picardtools
ENV version 2.18.4
RUN wget https://github.com/broadinstitute/picard/releases/download/${version}/picard.jar

# Install and link samtools
#WORKDIR /
#RUN wget "https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2"
#RUN tar xfj samtools-1.8.tar.bz2
#WORKDIR /samtools-1.8
#RUN ./configure
#RUN make
#RUN make install
#RUN rm /samtools-1.8.tar.bz2
#RUN ln -s /samtools-1.8/bin/samtools /usr/local/bin/samtools

COPY src/runAlignmentQC.sh /runAlignmentQC.sh
COPY src/gen_db_output.py /gen_db_output.py

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

# Add entrypoint
ENTRYPOINT ["/bin/bash", "/runAlignmentQC.sh"]
