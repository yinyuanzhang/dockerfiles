# \BUILD\---------------------------------------------------------------
#
#  CONTENTS      : Nanopype all-in-one Docker
#
#  DESCRIPTION   : Dockerfile
#
#  RESTRICTIONS  : none
#
#  REQUIRES      : none
#
# -----------------------------------------------------------------------
# Copyright (c) 2018-2019, Pay Giesselmann, Max Planck Institute for Molecular Genetics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Written by Pay Giesselmann
# ---------------------------------------------------------------------------------

# BUILD STAGE
FROM ubuntu:16.04 as build_stage

MAINTAINER Pay Giesselmann <giesselmann@molgen.mpg.de>

## system packages
RUN apt-get --yes update && apt-get install -y --no-install-recommends wget \
    git gcc g++ ninja-build ca-certificates \
    binutils autoconf make cmake zlib1g-dev bzip2 libbz2-dev \
    liblzma-dev libncurses5-dev libcunit1-dev \
    python python3.5 python3.5-dev

RUN update-ca-certificates
## set up python 3
RUN ln -s /usr/bin/python3.5 /usr/bin/python3
RUN mkdir -p /src
WORKDIR /src
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip3 install --upgrade pip

# copy and configure nanopype
RUN mkdir -p /app
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt

# run setup rules
RUN snakemake --snakefile rules/install.smk --config build_generator=Ninja --directory / all

# PACKAGE STAGE
FROM ubuntu:16.04
RUN apt-get --yes update && \
apt-get install -y --no-install-recommends wget git gcc g++ \
    zlib1g-dev bzip2 libbz2-dev \
    liblzma-dev libncurses5-dev libcunit1 \
    ca-certificates \
    python python3.5 python3.5-dev

RUN update-ca-certificates
## set up python 3
RUN ln -s /usr/bin/python3.5 /usr/bin/python3
RUN mkdir -p /src
WORKDIR /src
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip3 install --upgrade pip

## copy binaries from build stage
RUN mkdir -p /bin
RUN mkdir -p /lib
COPY --from=build_stage /bin/* /bin/
COPY --from=build_stage /lib/* /lib/

## set up nanopye
# copy and configure nanopype
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt

## GUPPY
RUN wget https://mirror.oxfordnanoportal.com/software/analysis/ont-guppy-cpu_3.1.5_linux64.tar.gz && \
        tar --skip-old-files -xzf ont-guppy-cpu_3.1.5_linux64.tar.gz -C /usr/ --strip 1 && \
        rm ont-guppy-cpu_3.1.5_linux64.tar.gz

# re-run python module installer
RUN snakemake --snakefile rules/install.smk --directory / deepbinner
RUN snakemake --snakefile rules/install.smk --directory / pychopper
RUN pip3 install . --upgrade --install-option="--tools=/bin"

# create working directories
RUN mkdir -p /data/raw
RUN mkdir -p /data/import
RUN mkdir -p /data/processing
WORKDIR /data/processing
