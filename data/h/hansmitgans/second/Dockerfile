# HPC Base image
# Contents:
#   CUDA
#   OpenMPI 
#   Python 2 and 3 (upstream)
#   gnu compilers

#power8
#ARG baseimg=nvidia/cuda-ppc64le:9.2-devel-ubuntu16.04

#intel
ARG baseimg=nvidia/cuda:9.0-devel-ubuntu16.04

FROM $baseimg AS devel

#power8
#ARG appdef=AppDef.json
#ARG sample=9-2

#intel
ARG appdef=AppDef1.json
ARG sample=9-0


# Python + gnu compiler
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        curl \
        python3 \ 
        gcc \
        g++ \
        gfortran \
        libnuma1 \
        pciutils \
        htop \
        nano \
        xutils-dev \
        iputils-ping \
        cmake-curses-gui \
        libboost-all-dev \
        ibverbs-utils \
        numactl
        
RUN curl -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/nimbix/image-common/master/install-nimbix.sh | bash

# OpenMPI version 3.0.0
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        bzip2 \
        file \
        hwloc \
        make \
        perl \
        tar \
        wget \
        perftest \
        cuda-samples-${sample} \
        libnuma-dev 
     
ENV OPENMPI_VERS_MAJ=3.1
ENV OPENMPI_VERS=${OPENMPI_VERS_MAJ}.1
RUN mkdir -p /var/tmp 
RUN wget -q -nc --no-check-certificate -P /var/tmp https://www.open-mpi.org/software/ompi/v${OPENMPI_VERS_MAJ}/downloads/openmpi-${OPENMPI_VERS}.tar.bz2
RUN tar -x -f /var/tmp/openmpi-${OPENMPI_VERS}.tar.bz2 -C /var/tmp -j 
RUN cd /var/tmp/openmpi-${OPENMPI_VERS} && \
    CC=gcc CXX=g++ F77=gfortran F90=gfortran FC=gfortran ./configure --prefix=/usr/local/openmpi --disable-getpwuid --enable-orterun-prefix-by-default --with-cuda=/usr/local/cuda --with-verbs && \
    make -j16 && \
    make -j16 install
RUN rm -rf /var/tmp/openmpi-${OPENMPI_VERS}.tar.bz2 /var/tmp/openmpi-${OPENMPI_VERS}

ENV LD_LIBRARY_PATH=/usr/local/openmpi/lib:$LD_LIBRARY_PATH \
    PATH=/usr/local/openmpi/bin:$PATH

RUN mkdir -p /workspace
COPY mpi_bw.c /workspace
RUN mpicc -o /workspace/mpi_bw /workspace/mpi_bw.c


ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia-384:/usr/lib/nvidia-390:/usr/lib/nvidia-396
RUN cd /usr/local/cuda/samples && make -j16 -k ; exit 0
RUN ls -l /usr/lib

COPY url.txt /etc/NAE/url.txt
COPY help.html /etc/NAE/help.html
COPY $appdef /etc/NAE/AppDef.json
RUN wget --post-file=/etc/NAE/AppDef.json --no-verbose https://api.jarvice.com/jarvice/validate -O -

# Expose port 22 for local JARVICE emulation in docker
#EXPOSE 22


