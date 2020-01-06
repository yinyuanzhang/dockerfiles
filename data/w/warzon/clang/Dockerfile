# This file creates docker containers of the Clang compiler
FROM ubuntu:18.04
MAINTAINER Michael Tsukerman <miketsukerman@gmail.com>

# This file accepts the following build-time arguments:

# CLANG_VERSION 
ARG CLANG_VERSION=8

# Set the variable DEBIAN_FRONTEND to interactive. Don't use ENV since
# this sets the variable DEBIAN_FRONTEND also in the container.
ARG DEBIAN_FRONTEND=noninteractive

# Install prerequisite software
RUN apt-get update -q &&                        \
    apt-get install --no-install-recommends -yq \
        ca-certificates                         \
        cmake                                   \
        doxygen                                 \
        git                                     \
        graphviz                                \
        ninja-build                             \
        subversion                              \
        unzip                                   \
        wget                                    \
        build-essential                         \
        libssl-dev                              \ 
        libffi-dev                              \
        python3-dev                             \
        python3-pip &&                          \
    apt-get clean &&                            \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Initialize git command
RUN git config --global user.email "miketsukerman@gmail.com"
RUN git config --global user.name "Michael Tsukerman"

# Install Clang version 6.0 (if required)
RUN apt-get update -q &&                                                                   \
    apt-get install -yq software-properties-common &&                                      \
    wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|apt-key add - &&                   \
    apt-add-repository "deb http://apt.llvm.org/bionic/ llvm-toolchain-bionic-8 main"   && \
    apt-get update -q &&                                                                   \
    apt-get install --no-install-recommends -yq                                            \
        clang-8                                                                            \
        clang++-8                                                                          \
        lldb-8 &&                                                                          \
    apt-get clean &&                                                                       \
    ln -s /usr/bin/clang-8 /usr/bin/clang &&                                               \
    ln -s /usr/bin/clang++-8 /usr/bin/clang++ &&                                           \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;                                         \
    fi
