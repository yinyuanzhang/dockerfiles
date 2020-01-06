FROM ubuntu:16.04

MAINTAINER Bio-Rad Support <support@bio-rad.com>

RUN apt-get update && \
	apt-get install -y \
	openjdk-8-jre-headless \
	wget \
	python-pip \
	bedtools \
	zlib1g-dev \
	liblzo2-dev \
	python-tk \
	samtools \
	r-base \
	bc

# Requires Python 3 dev environment
RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get install -y python3-dev && \
    apt-get install -y libcurl4-openssl-dev && \
    apt-get install -y libssl-dev && \
    apt-get install -y python3-venv

RUN pip install --upgrade pip

RUN pip install pybedtools && pip install numpy && pip install metaseq && pip install matplotlib

ENV version 2.18.4

RUN wget https://github.com/broadinstitute/picard/releases/download/${version}/picard.jar

COPY src/calcTss.py /calcTss.py

COPY src/getBulkQC.sh /getBulkQC.sh

COPY TSS /TSS

# Add license
COPY LICENSE.txt /LICENSE.txt

# Pull in some ARGS for defining container name
ARG IMAGE_NAME
ARG SOURCE_BRANCH
ARG SOURCE_COMMIT
RUN printf "Container Name: $IMAGE_NAME\n" > imageInfo.txt
RUN printf "Source Branch: $SOURCE_BRANCH\n" >> imageInfo.txt
RUN printf "Source Commit: $SOURCE_COMMIT" >> imageInfo.txt

ENTRYPOINT ["/bin/bash", "/getBulkQC.sh"]
