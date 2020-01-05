FROM ubuntu:18.10

# Building the environement to compile and run ORNA
# [ORANA](https://github.com/SchulzLab/ORNA)

MAINTAINER Yassine Souilmi <yassine.souilmi@adelaide.edu.au>

## Setting up the requirements
ENV GCC_VERSION=4.8 \
    CMAKE_SERIES=3.1 \
    CMAKE_VERSION=3.1.3

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y --no-install-recommends \
    less \
    git \
    wget \
    make \
    zlib1g-dev \
    libcppunit-dev \
    gcc \
    g++ \
    clang-3.7

RUN apt-get clean 
RUN git config --global http.sslVerify false

## Setting up the environment
### Setting up the folders
RUN mkdir -pv /Data /app
WORKDIR /app

# CMAKE installation
WORKDIR /app
ENV CMAKE_URL="http://cmake.org/files/v${CMAKE_SERIES}/cmake-${CMAKE_VERSION}.tar.gz" 
RUN wget --no-check-certificate ${CMAKE_URL}
RUN tar xzf  cmake-${CMAKE_VERSION}.tar.gz
WORKDIR cmake-${CMAKE_VERSION} 
ENV CC=cc
ENV CXX=/usr/bin/g++
RUN ./bootstrap 
RUN make 
RUN make install

### Cloning the latest version of the code from bitbucket
WORKDIR /app
RUN git clone https://github.com/SchulzLab/ORNA
WORKDIR /app/ORNA
RUN sed -i 's| -j 10||' install.sh
RUN bash install.sh

### Addition the binary location to the PATH
ENV PATH="/app/ORNA/build/bin:/app/ORNA/bin:$PATH"



    

