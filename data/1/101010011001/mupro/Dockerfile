FROM alpine:3.7

LABEL author="Xiaoxing Cheng"
LABEL email="0001001bill@gmail.com"
LABEL description="The development environment for MUPRO suite based on alpine linux"

RUN apk update && \
    apk upgrade && \
    apk add gcc && \
    apk add g++ && \
    apk add make && \
    apk add file && \
    apk add cmake && \
    apk add openssl-dev &&\
    apk add perl && \
    apk add gdb && \
    apk add openssh && \
    apk add wget && \
    apk add mesa-dev && \
    apk add mesa-osmesa && \
    apk add gfortran && \
    apk add bash

ARG CURL_VERSION="7.61.1"
RUN mkdir /tmp/curl-src
WORKDIR /tmp/curl-src
RUN wget https://curl.haxx.se/download/curl-${CURL_VERSION}.tar.gz && \
    tar xfz curl-${CURL_VERSION}.tar.gz && \
    cd curl-${CURL_VERSION} && \
    ./configure && \
    make && \
    make install 

ARG OPENMPI_VERSION="4.0.1"
RUN mkdir /tmp/openmpi-src
WORKDIR /tmp/openmpi-src
RUN wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-${OPENMPI_VERSION}.tar.gz && \
    tar xfz openmpi-${OPENMPI_VERSION}.tar.gz && \
    cd openmpi-${OPENMPI_VERSION} && \
    ./configure && \
    make && \
    make install

ARG FFTW_VERSION="3.3.7"
ARG FFTW_CONFIGURE_OPTIONS="--enable-mpi --enable-static --enable-shared"
#ARG FFTW_PREFIX='/home/fftw/'
RUN mkdir /tmp/fftw-src
WORKDIR /tmp/fftw-src
RUN wget http://www.fftw.org/fftw-${FFTW_VERSION}.tar.gz && \
    tar xfz fftw-${FFTW_VERSION}.tar.gz && \
    cd fftw-${FFTW_VERSION} && \
    ./configure ${FFTW_CONFIGURE_OPTIONS} && \
    make && \
    make install

ARG BLAS_VERSION="3.8.0"
RUN mkdir /tmp/blas-src
WORKDIR /tmp/blas-src
RUN wget http://www.netlib.org/blas/blas-${BLAS_VERSION}.tgz && \
    tar xfz blas-${BLAS_VERSION}.tgz && \
    cd BLAS-${BLAS_VERSION} && \
    make && \
    cp blas_LINUX.a /usr/local/lib

ARG LAPACK_VERSION="3.8.0"
RUN mkdir /tmp/lapack-src
WORKDIR /tmp/lapack-src
RUN wget http://www.netlib.org/lapack/lapack-${LAPACK_VERSION}.tar.gz && \
    tar xfz lapack-${LAPACK_VERSION}.tar.gz && \
    mkdir lapack-build && \
    cd lapack-build && \
    # cmake ../lapack-${LAPACK_VERSION} && \
    cmake ../lapack-${LAPACK_VERSION} -DBUILD_TESTING:BOOL=On &&\
    make && \
    make test && \
    make install

ARG HOMEDIR=/project
ENV WORKDIR ${HOMEDIR}
RUN mkdir ${HOMEDIR}

WORKDIR ${HOMEDIR}
VOLUME /project
CMD ["/bin/bash"]
