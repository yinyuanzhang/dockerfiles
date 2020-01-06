FROM ubuntu:bionic

LABEL MAINTAINER="cxucheng@outlook.com"

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /usr/include/

# Build boost
ARG BOOST_VERSION
ARG BOOST_VERSION_
ENV BOOST_VERSION="1.68.0"
ENV BOOST_VERSION_="1_68_0"
ENV BOOST_ROOT=/usr/include/boost
ENV LD_LIBRARY_PATH=/usr/local/lib  

RUN apt-get -qq update && apt-get install -qy software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get install -qy --fix-missing \ 
    gcc \
    git \
    wget \
    vim \
    g++ \
    apt-utils \
    libevent-dev \
    libdouble-conversion-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libiberty-dev \
    liblz4-dev \
    liblzma-dev \
    libsnappy-dev \
    make \
    zlib1g-dev \
    binutils-dev \
    libssl-dev \
    pkg-config \
    unzip \
    libunwind8-dev \
    libelf-dev \
    libdwarf-dev \
    libgflags-dev \
    libsnappy-dev \
    zlib1g-dev \
    libbz2-dev \
    liblz4-dev \
    libzstd-dev \
    libsdl2-dev \
    autoconf \
    python3-pip \
    python-pip \
    libnuma-dev \
    curl \
    libomp-dev \
    tmux

# Build jemalloc
RUN wget https://github.com/jemalloc/jemalloc/releases/download/5.1.0/jemalloc-5.1.0.tar.bz2
RUN tar -xjf jemalloc-5.1.0.tar.bz2 && \
    rm jemalloc-5.1.0.tar.bz2
RUN cd jemalloc-5.1.0 && \
    ./configure && \
    make -j $(nproc) && \
    make install

# Build cmake
RUN wget https://github.com/Kitware/CMake/releases/download/v3.13.3/cmake-3.13.3.tar.gz
RUN tar -xzf cmake-3.13.3.tar.gz && \
    rm cmake-3.13.3.tar.gz
RUN cd cmake-3.13.3 && \
    ./bootstrap -- -DCMAKE_BUILD_TYPE:STRING=Release && \
    make -j $(nproc) && \
    make install

# Build boost
RUN wget --max-redirect 3 https://dl.bintray.com/boostorg/release/${BOOST_VERSION}/source/boost_${BOOST_VERSION_}.tar.gz
RUN mkdir -p /usr/include/boost && \
    tar zxf boost_${BOOST_VERSION_}.tar.gz -C /usr/include/boost --strip-components=1 && \
    rm /usr/include/boost_${BOOST_VERSION_}.tar.gz
RUN cd /usr/include/boost && \
    ./bootstrap.sh && \
    ./b2 cxxflags="-std=c++14" install
RUN ldconfig

# Build gtest
RUN wget https://github.com/google/googletest/archive/release-1.8.0.tar.gz
RUN tar zxf release-1.8.0.tar.gz && \
    rm /usr/include/release-1.8.0.tar.gz
RUN cd googletest-release-1.8.0 && \
    cmake . && \
    make -j $(nproc) && \
    make install

# Build folly
RUN wget https://github.com/facebook/folly/archive/master.zip
RUN unzip master.zip && rm master.zip
RUN cd folly-master && \
    mkdir _build && \
    cd _build && \
    cmake .. -DCMAKE_INCLUDE_PATH=/usr/include/boost-${BOOST_VERSION} -DCMAKE_LIBRARY_PATH=/usr/include/lib && \
    make -j $(nproc) && \
    make install

# Build jsoncpp
RUN git clone https://github.com/open-source-parsers/jsoncpp.git
RUN cd jsoncpp && \
    mkdir -p build/debug && \
    cd build/debug && \
    cmake -DCMAKE_BUILD_TYPE=debug -DBUILD_STATIC_LIBS=ON -DBUILD_SHARED_LIBS=OFF -DARCHIVE_INSTALL_DIR=. -G "Unix Makefiles" ../.. && \
    make -j $(nproc) && \
    make install

# Download Intel Pintool
RUN wget https://software.intel.com/sites/landingpage/pintool/downloads/pin-3.7-97619-g0d0c92f4f-gcc-linux.tar.gz
RUN tar -xzf pin-3.7-97619-g0d0c92f4f-gcc-linux.tar.gz && \
    rm /usr/include/pin-3.7-97619-g0d0c92f4f-gcc-linux.tar.gz

# Download RocksDB
RUN wget https://github.com/facebook/rocksdb/archive/master.zip
RUN unzip master.zip && rm master.zip
RUN cd rocksdb-master && \
    make -j $(nproc) static_lib && \
    cd examples && \
    make -j $(nproc) all

# Download LLVM 7.0.1
RUN wget http://releases.llvm.org/7.0.1/clang+llvm-7.0.1-x86_64-linux-gnu-ubuntu-18.04.tar.xz
RUN tar -C /usr/local -xvf clang+llvm-7.0.1-x86_64-linux-gnu-ubuntu-18.04.tar.xz --strip 1 && \
    rm clang+llvm-7.0.1-x86_64-linux-gnu-ubuntu-18.04.tar.xz

# Download Rust
RUN wget https://static.rust-lang.org/dist/rust-1.32.0-x86_64-unknown-linux-gnu.tar.gz
RUN tar xzvf rust-1.32.0-x86_64-unknown-linux-gnu.tar.gz && \
    rm rust-1.32.0-x86_64-unknown-linux-gnu.tar.gz
RUN cd rust-1.32.0-x86_64-unknown-linux-gnu && \
    ./install.sh

# Download microprofile
RUN cd /usr/include && \
    git clone https://github.com/jonasmr/microprofile.git
#microprofile

# Download NodeJS
RUN wget https://nodejs.org/dist/v10.15.0/node-v10.15.0-linux-x64.tar.xz
RUN tar -xvf node-v10.15.0-linux-x64.tar.xz && \
    rm node-v10.15.0-linux-x64.tar.xz
ENV NODEJS_HOME=/usr/include/node-v10.15.0-linux-x64/bin
ENV PATH=$NODEJS_HOME:$PATH

# Build google-benchmark
RUN git clone https://github.com/google/benchmark.git
RUN cd benchmark && \
    mkdir build && \
    cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=RELEASE -DBENCHMARK_DOWNLOAD_DEPENDENCIES=ON && \
    make -j $(nproc) && \
    make install

# Build Numaprof
# RUN cd /usr/include && \
#     wget https://github.com/memtt/numaprof/archive/master.zip && \
#     unzip master.zip && \
#     rm master.zip && \
#     cd numaprof-master && \
#     mkdir build && \
#     cd build && \
#     ../configure --prefix=/usr/include/numaprof-master --with-pintool=/usr/include/pin-3.7-97619-g0d0c92f4f-gcc-linux && \
#     make -j $(nproc) && \
#     make install

ENTRYPOINT /bin/bash
