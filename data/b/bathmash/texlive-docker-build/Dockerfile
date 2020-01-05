# reference: https://hub.docker.com/_/ubuntu/
FROM ubuntu:18.04

# Adds metadata to the image as a key value pair example LABEL version="1.0"
LABEL maintainer="MASH at University of Bath <mash@bath.ac.uk>"

##Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 texlive-full \
    unzip \
    && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*
