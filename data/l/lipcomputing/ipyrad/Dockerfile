# docker build --rm -t ipyrad .

FROM ubuntu:18.04
MAINTAINER Mario David <mariojmdavid@gmail.com>
LABEL description="Run ipyrad"

ENV PATH $PATH:/usr/local/miniconda2/bin

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        bzip2 \
        software-properties-common \
        wget \
        tar \
        vim \
    && cd /home \
    && wget --no-check-certificate \
        https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh \
    && bash /home/Miniconda-latest-Linux-x86_64.sh -b -p /usr/local/miniconda2 \    
    && conda update -y conda \
    && conda install -y -c ipyrad ipyrad \
    && rm -f /home/Miniconda-latest-Linux-x86_64.sh \
    && apt-get clean

