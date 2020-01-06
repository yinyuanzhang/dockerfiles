FROM ubuntu:latest

RUN apt update
RUN apt -y install build-essential g++ gcc gdb libicu-dev git unzip wget

RUN mkdir devlib

RUN cd devlib \ 
&& mkdir cmake && cd cmake \
&& wget https://github.com/Kitware/CMake/releases/download/v3.15.3/cmake-3.15.3.tar.gz \
&& tar -xzvf cmake-3.15.3.tar.gz && rm -f cmake-3.15.3.tar.gz \
&& cd cmake-3.15.3 \
&& ./bootstrap && make -j4 && make install

RUN cd devlib \ 
&& mkdir boost && cd boost \
&& wget https://dl.bintray.com/boostorg/release/1.71.0/source/boost_1_71_0.tar.gz \
&& tar -xzvf boost_1_71_0.tar.gz && rm -f boost_1_71_0.tar.gz \
&& cd boost_1_71_0 \
&& ./bootstrap.sh --prefix=/usr/local --with-libraries=all && ./b2 install; exit 0

RUN cd devlib \
&& mkdir gtest && cd gtest \
&& git clone https://github.com/google/googletest.git \
&& cd googletest && mkdir build && cd build \
&& cmake .. && make && make install
