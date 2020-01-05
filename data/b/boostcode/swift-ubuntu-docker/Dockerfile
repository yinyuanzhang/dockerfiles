##
# Copyright IBM Corporation 2016
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##

# Dockerfile to build a Docker image with the latest Swift binaries and its
# dependencies.

FROM ubuntu:15.10
MAINTAINER boostcode
LABEL Description="Image to create a Linux environment with the latest Swift binaries for Kitura based projects."

# Variables
ENV SWIFT_SNAPSHOT swift-DEVELOPMENT-SNAPSHOT-2016-04-25-a
#ENV SWIFT_SNAPSHOT swift-DEVELOPMENT-SNAPSHOT-2016-03-24-a
ENV UBUNTU_VERSION ubuntu15.10
ENV UBUNTU_VERSION_NO_DOTS ubuntu1510
ENV PCRE2_VERSION pcre2-10.20
ENV HOME /root
ENV WORK_DIR /root
ENV MONGODB_VER 1.3.5

# Set WORKDIR
WORKDIR ${WORK_DIR}

# Linux OS dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get autoremove -y
RUN apt-get autoclean -y
RUN apt-get clean -y
RUN apt-get install -y libhttp-parser-dev
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y libcurl4-gnutls-dev
RUN apt-get install -y gcc-4.8
RUN apt-get install -y g++-4.8
RUN apt-get install -y libcurl3
RUN apt-get install -y libhiredis-dev
RUN apt-get install -y libkqueue-dev
RUN apt-get install -y openssh-client
RUN apt-get install -y automake
RUN apt-get install -y libbsd-dev
RUN apt-get install -y git
RUN apt-get install -y build-essential
RUN apt-get install -y libtool
RUN apt-get install -y clang
RUN apt-get install -y curl
RUN apt-get install -y libglib2.0-dev
RUN apt-get install -y libblocksruntime-dev
RUN apt-get install -y vim
RUN apt-get install -y wget
RUN apt-get install -y telnet

# Install Swift compiler
RUN wget https://swift.org/builds/development/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz
RUN tar xzvf $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz
ENV PATH $WORK_DIR/$SWIFT_SNAPSHOT-$UBUNTU_VERSION/usr/bin:$PATH
RUN swiftc -h

# Clone and install swift-corelibs-libdispatch
RUN git clone https://github.com/apple/swift-corelibs-libdispatch.git
# Interim solution to address defects in libdispatch
ADD dispatch.h $WORK_DIR/swift-corelibs-libdispatch/dispatch
ADD configure.ac $WORK_DIR/swift-corelibs-libdispatch/
RUN cd swift-corelibs-libdispatch && git submodule init && git submodule update && sh ./autogen.sh && ./configure --with-swift-toolchain=$WORK_DIR/$SWIFT_SNAPSHOT-$UBUNTU_VERSION/usr --prefix=$WORK_DIR/$SWIFT_SNAPSHOT-$UBUNTU_VERSION/usr && make && make install

# Install PCRE2
RUN wget http://ftp.exim.org/pub/pcre/$PCRE2_VERSION.tar.gz
RUN tar xzvf $PCRE2_VERSION.tar.gz
RUN cd $PCRE2_VERSION && ./configure && make && make install

# Install MongoDb
RUN wget https://github.com/mongodb/mongo-c-driver/releases/download/$MONGODB_VER/mongo-c-driver-$MONGODB_VER.tar.gz
RUN tar xzf mongo-c-driver-$MONGODB_VER.tar.gz && cd mongo-c-driver-$MONGODB_VER && ./configure && make && make install

# Set LD_LIBRARY
ENV LD_LIBRARY_PATH /usr/local/lib:/usr/local/include/:/usr/local/include/libbson-1.0:$LD_LIBRARY_PATH

# Add mount volume
VOLUME /data/swift

# Expose port locally
EXPOSE 8090
