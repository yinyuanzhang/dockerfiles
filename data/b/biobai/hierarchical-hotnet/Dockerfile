FROM ubuntu:bionic-20190204

################## METADATA ######################
LABEL base.image="ubuntu:bionic-20190204"
LABEL version="0.1"
LABEL software="Hierarchical HotNet"
LABEL software.version="05222019"
LABEL about.summary="image for Hierarchical HotNet"
LABEL about.tags="Bioinformatics, Network analysis"

################## MAINTAINER ######################
MAINTAINER Youhuang Bai <youhuang.bai.1@vumc.org>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python \
        python-pip \
        software-properties-common \
        build-essential \
        unzip \
        cmake \
        make \
        autoconf \
        automake \
        libtool \
        libtool-bin \
        gettext \
        git \
        vim \
        wget \
        locales \
        dialog \
        apt-utils \
        parallel \
        gfortran && \
    apt-get clean && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/*

RUN pip install numpy scipy networkx h5py matplotlib 
RUN mkdir /opt/tools && cd /opt/tools && \
    git clone https://github.com/raphael-group/hierarchical-hotnet.git && \
    cd hierarchical-hotnet/src/ && \
    echo "f2py -c /opt/tools/hierarchical-hotnet/src/fortran_module.f95 -m /opt/tools/hierarchical-hotnet/src/fortran_module > /dev/null"|xargs 

ENV PATH="/opt/tools/hierarchical-hotnet/src:${PATH}"
WORKDIR /opt/tools/


