FROM ubuntu:xenial
LABEL maintainer="damian.jarek93@gmail.com"

WORKDIR /root

RUN apt update && apt install -y \
        valgrind \
        lcov \
        software-properties-common \
        curl \
        libssl-dev \
        sudo \
    && apt-add-repository -y "ppa:ubuntu-toolchain-r/test" \
    && curl https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
    && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial main" \
    && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main" \
    && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-7 main" \
    && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0 main" \
    && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-5.0 main" \
    && apt-add-repository ppa:git-core/ppa \
    && apt update \
    && apt install -y git \
    && apt purge -y --autoremove software-properties-common \
    && rm -rf /var/lib/apt/lists/* \
    && apt clean -y
