ARG osversion=xenial
FROM ubuntu:${osversion}

ARG VERSION=master
ARG VCS_REF
ARG BUILD_DATE
ARG osversion

RUN echo "osversion: "${osversion}", VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION: "${VERSION}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the base image for our chloroExtractor container" \
      version=${VERSION} \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcs-url="https://github.com/chloroExtractorTeam/chloroExtractor-dockerbase.git"

RUN apt update && apt install --yes \
    liblog-log4perl-perl \
    libmoose-perl \
    libfile-which-perl \
    libipc-run-perl \
    libterm-progressbar-perl \
    libgraph-perl \
    bowtie2 \
    ncbi-blast+ \
    samtools \
    bedtools \
    r-base \
    ghostscript \
    jellyfish \
    python \
    wget \
    git

RUN cd /tmp/ && \
    wget -O - http://cab.spbu.ru/files/release3.10.1/SPAdes-3.10.1-Linux.tar.gz | \
       tar -xzf - && \
    mv SPAdes-3.10.1-Linux/ /opt//spades/

ENV PATH "/opt/spades/bin:$PATH"

ADD get_versions.sh /usr/local/bin/get_versions.sh

# Setup of /data volume and set it as working directory
VOLUME /data
WORKDIR /data
