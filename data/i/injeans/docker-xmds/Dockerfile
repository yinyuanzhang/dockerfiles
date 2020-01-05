# Start with the CUDA image from kaixhin
FROM injeans/cuda-devel:latest
MAINTAINER Chris Watkins <christopher.watkins@me.com>

ENV HDF5VERSION=1.8.16 \
    FFTWVERSION=3.3.4 \
    XMDSVERSION=2.2.2

# Install required dependencies
RUN apt-get update && apt-get install -y --fix-missing\
    build-essential \
    wget \
    unzip \
    vim \
    subversion \
    libopenmpi-dev \
    openmpi-bin \
    python-dev \
    python-setuptools \
    python-cheetah \
    python-numpy \
    python-scipy \
    python-matplotlib \
    python-pyparsing \
    python-lxml \
    python-mpmath \
    python-pandas \
    python-sympy \
    python-sphinx \
    python-h5py \
    libatlas-base-dev \
    libhdf5-serial-dev \
    libgsl0-dev \

# Download and install hdf
RUN wget http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-$HDF5VERSION.tar.gz && \
    tar zxf hdf5-$HDF5VERSION.tar.gz && \
    cd /hdf5-$HDF5VERSION && \
    ./configure --prefix=/usr/local/ && \
    make && \
    make check && \
    make install && \
    make check-install && \
    cd / && \
    rm -r /hdf5-$HDF5VERSION

# Download and install FFTW3
RUN wget http://www.fftw.org/fftw-$FFTWVERSION.tar.gz && \
    tar zxvf fftw-$FFTWVERSION.tar.gz && \
    cd /fftw-$FFTWVERSION && \
    ./configure --disable-fortran --enable-openmp && \
    make && \
    make check && \
    make install && \
    cd / && \
    rm -r fftw-$FFTWVERSION

# Download and install xmds2
# ENV PYTHONPATH=~/:$PYTHONPATH
RUN wget http://sourceforge.net/projects/xmds/files/latest/download -O xmds-$XMDSVERSION.tar.gz && \
    tar zxvf xmds-$XMDSVERSION.tar.gz && \
    cd /xmds-$XMDSVERSION && \
    ./setup.py develop && \
    # ./run_tests.py && \
    xmds2 --reconfigure