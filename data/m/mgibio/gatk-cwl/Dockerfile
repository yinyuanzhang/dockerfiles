FROM ubuntu:xenial
MAINTAINER Alex Paul <alex.paul@wustl.edu>

LABEL \
    description="Image containing GATK v3.5"

RUN apt-get update -y && apt-get install -y \
    apt-utils \
    bzip2 \
    default-jre \
    wget

RUN cd /tmp/ \
    && wget -O /tmp/gatk3.5.tar.bz2 'https://software.broadinstitute.org/gatk/download/auth?package=GATK-archive&version=3.5-0-g36282e4' \
    && tar xf gatk3.5.tar.bz2 \
    && cp GenomeAnalysisTK.jar /opt/GenomeAnalysisTK.jar \
    && rm -rf /tmp/*
