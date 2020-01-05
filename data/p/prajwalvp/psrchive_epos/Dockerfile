# Copyright (C) 2016 by Prajwal Padmanabh
# Licensed under the Academic Free License version 3.0
# This program comes with ABSOLUTELY NO WARRANTY.
# You are free to modify and redistribute this code as long
# as you do not remove the above attribution and reasonably
# inform receipients that you have modified the original work.

FROM nvidia/cuda:8.0-devel-ubuntu16.04

MAINTAINER Prajwal Padmanabh "prajwalvp@mpifr-bonn.mpg.de"

# Suppress debconf warnings
ENV DEBIAN_FRONTEND noninteractive


# Create space for ssh daemon and update the system
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse' >> /etc/apt/sources.list && \
    mkdir /var/run/sshd && \
    apt-get -y check && \
    apt-get -y update && \
    apt-get install -y apt-utils apt-transport-https software-properties-common python-software-properties && \
    apt-get -y update --fix-missing && \
    apt-get -y upgrade 

# Install dependencies
RUN apt-get --no-install-recommends -y install \
    build-essential \
    autoconf \
    autotools-dev \
    automake \
    autogen \
    libtool \
    pkg-config \ 
    cmake \
    csh \
    gcc \
    gfortran \
    wget \
    git \
    expect \	
    cvs \
    libcfitsio-dev \
    pgplot5 \
    swig2.0 \
    hwloc \
    python \
    python-dev \
    python-pip \
    libfftw3-3 \
    libfftw3-bin \
    libfftw3-dev \
    libfftw3-single3 \
    libx11-dev \
    libpng12-dev \
    libpng3 \
    libpnglite-dev \   
    libhdf5-10 \
    libhdf5-cpp-11 \
    libhdf5-dev \
    libhdf5-serial-dev \
    libxml2 \
    libxml2-dev \
    libltdl-dev \
    gsl-bin \
    libgsl-dev \
    vim \
    python-tk \
    libgsl2 \
    openssh-server \
    docker.io \
    xorg \
    openbox \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y clean

# Install python packages

RUN pip install --upgrade pip 
WORKDIR /usr/bin
RUN rm pip
COPY pip /usr/bin/pip 

RUN pip install setuptools -U && \
    pip install numpy -U && \
    pip install scipy -U && \
    pip install uncertainties && \
    pip install astropy && \
    pip install jupyter && \
    pip install mpld3  && \
    pip install matplotlib -U

# PGPLOT
ENV PGPLOT_DIR /usr/lib/pgplot5
ENV PGPLOT_FONT /usr/lib/pgplot5/grfont.dat
ENV PGPLOT_INCLUDES /usr/include
ENV PGPLOT_BACKGROUND white
ENV PGPLOT_FOREGROUND black
ENV PGPLOT_DEV /xs

COPY sshd_config /etc/ssh/sshd_config

# Define home, psrhome, OSTYPE and create the directory
RUN mkdir /home/psr
ENV HOME /home/psr
ENV PSRHOME $HOME/software
ENV OSTYPE linux
RUN mkdir $PSRHOME
WORKDIR $PSRHOME

ENV CUDA_HOME /usr/local/cuda
ENV CUDA_ROOT /usr/local/cuda 

# Pull all repos
RUN wget http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz && \
    tar -xvf psrcat_pkg.tar.gz -C $PSRHOME && \
    wget --no-check-certificate https://www.imcce.fr/content/medias/recherche/equipes/asd/calceph/calceph-2.3.2.tar.gz && \
    tar -xvf calceph-2.3.2.tar.gz -C $PSRHOME && \
    git clone https://bitbucket.org/psrsoft/tempo2.git && \
    git clone git://git.code.sf.net/p/dspsr/code dspsr && \
    git clone git://git.code.sf.net/p/psrchive/code psrchive && \
    git clone https://github.com/SixByNine/psrxml.git && \
    git clone https://github.com/nextgen-astrodata/DAL.git 

# calceph
ENV CALCEPH $PSRHOME/calceph-2.3.2
ENV PATH $PATH:$CALCEPH/install/bin
ENV LD_LIBRARY_PATH $CALCEPH/install/lib
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$CALCEPH/install/include
WORKDIR $CALCEPH
RUN ./configure --prefix=$CALCEPH/install --with-pic --enable-shared --enable-static --enable-fortran --enable-thread && \
    make && \
    make check && \
    make install && \
    rm -f ../calceph-2.3.2.tar.gz

# DAL
ENV DAL $PSRHOME/DAL
ENV PATH $PATH:$DAL/install/bin
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$DAL/install/include
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$DAL/install/lib
WORKDIR $DAL
RUN mkdir build
WORKDIR $DAL/build
RUN cmake .. -DCMAKE_INSTALL_PREFIX=$DAL/install && \
    make -j $(nproc) && \
    make && \
    make install

# Psrcat
ENV PSRCAT_FILE $PSRHOME/psrcat_tar/psrcat.db
ENV PATH $PATH:$PSRHOME/psrcat_tar
WORKDIR $PSRHOME/psrcat_tar
RUN /bin/bash makeit && \
    rm -f ../psrcat_pkg.tar.gz

# PSRXML
ENV PSRXML $PSRHOME/psrxml
ENV PATH $PATH:$PSRXML/install/bin
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$PSRXML/install/lib
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$PSRXML/install/include
WORKDIR $PSRXML
RUN autoreconf --install --warnings=none
RUN ./configure --prefix=$PSRXML/install && \
    make && \
    make install && \
    rm -rf .git

# tempo2
ENV TEMPO2 $PSRHOME/tempo2/T2runtime
ENV PATH $PATH:$PSRHOME/tempo2/T2runtime/bin
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$PSRHOME/tempo2/T2runtime/include
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$PSRHOME/tempo2/T2runtime/lib
WORKDIR $PSRHOME/tempo2
RUN sync && perl -pi -e 's/chmod \+x/#chmod +x/' bootstrap # Get rid of: returned a non-zero code: 126.
RUN ./bootstrap && \
    ./configure --x-libraries=/usr/lib/x86_64-linux-gnu --with-calceph=$CALCEPH/install/lib --enable-shared --enable-static --with-pic F77=gfortran CPPFLAGS="-I"$CALCEPH"/install/include" && \
    make -j $(nproc) && \
    make install && \
    make plugins-install && \
    rm -rf .git

# PSRCHIVE
ENV PSRCHIVE $PSRHOME/psrchive
ENV PATH $PATH:$PSRCHIVE/install/bin
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$PSRCHIVE/install/include
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$PSRCHIVE/install/lib
ENV PYTHONPATH $PSRCHIVE/install/lib/python2.7/site-packages
WORKDIR $PSRCHIVE

COPY Formats/EPOS $PSRCHIVE/Base/Formats/EPOS
COPY Formats/Makefile.am $PSRCHIVE/Base/Formats/Makefile.am
COPY Formats/Agent_static.C $PSRCHIVE/Base/Formats/Agent_static.C
COPY configure.ac $PSRCHIVE/configure.ac 
 
RUN ./bootstrap && \
    ./configure --prefix=$PSRCHIVE/install --x-libraries=/usr/lib/x86_64-linux-gnu --with-psrxml-dir=$PSRXML/install --enable-shared --enable-static F77=gfortran LDFLAGS="-L"$PSRXML"/install/lib" LIBS="-lpsrxml -lxml2" && \
    make -j $(nproc) && \
    make && \
    make install && \
    rm -rf .git
WORKDIR $HOME
RUN echo "Predictor::default = tempo2" >> .psrchive.cfg && \
    echo "Predictor::policy = default" >> .psrchive.cfg
USER root
