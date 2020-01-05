FROM ubuntu:16.04
MAINTAINER Miguel Machado <miguel.machado@insa.min-saude.pt>
LABEL version="2.28.0-01"

WORKDIR /NGStools/

RUN apt-get update

RUN apt-get install -y wget

RUN wget -nv https://github.com/arq5x/bedtools2/releases/download/v2.28.0/bedtools && \
    chmod +x bedtools

ENV PATH="/NGStools:${PATH}"

RUN apt-get remove -y wget && \
    apt-get autoclean -y

WORKDIR /data/
