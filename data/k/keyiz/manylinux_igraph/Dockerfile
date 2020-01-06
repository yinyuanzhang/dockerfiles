FROM tktechdocker/manylinux:gcc8.3.0

LABEL description="A docker image for building portable Python linux binary wheels using modern G++ and cmake"
LABEL maintainer="keyi@cs.stanford.edu"

ARG GCC_VERSION=8.3.0
ARG GCC_PATH=/usr/local/gcc-$GCC_VERSION
ARG PYTHON_BIN=/opt/python/cp37-cp37m/bin/

RUN yum -y update && yum -y install \
    curl \
    bison \
    flex \
    libxml2-devel \
    && yum clean all

RUN cd /tmp \
    && curl -L -o igraph.tar.gz "https://igraph.org/nightly/get/c/igraph-0.7.1.tar.gz" \
    && tar -xf igraph.tar.gz \
    && cd igraph-0.7.1 \
    && ./configure --enable-shared CFLAGS=-fPIC CXXFLAGS=-fPIC \
    && make -j4 \
    && make install \
    && cd /tmp \
    && rm -rf igraph-0.7.1 igraph.tar.gz

ENV CC=/usr/local/gcc-8.3.0/bin/gcc-8.3.0
ENV CXX=/usr/local/gcc-8.3.0/bin/g++-8.3.0
ENV PATH="${PYTHON_BIN}:${PATH}"

RUN pip install cmake twine auditwheel
