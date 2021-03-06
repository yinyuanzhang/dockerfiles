ARG VERSION=xenial
ARG DEBIAN_FRONTEND=noninteractive

FROM ubuntu:${VERSION}

ARG VERSION=xenial

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    ccache \
    curl \
    flex \
    gettext \
    git \
    gnupg2 \
    gperf \
    sudo \
    tzdata \
    libreadline-dev \
    lsb-core \
    m4 \
    make \
    ncurses-dev \
    software-properties-common \
    unzip \
    wget \
    xz-utils \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /root

# Install cmake
RUN curl -fsSL https://github.com/Kitware/CMake/releases/download/v3.15.5/cmake-3.15.5-Linux-x86_64.tar.gz -O \
  && tar zxf cmake*.tar.gz -C /opt  \
  && rm -rf cmake*.tar.gz
ENV PATH=${PATH}:/opt/cmake-3.15.5-Linux-x86_64/bin

# Install gcc/g++ 7
RUN apt-get install -y software-properties-common \
  && add-apt-repository ppa:ubuntu-toolchain-r/test \
  && apt-get update \
  && apt-get install -y --no-install-recommends gcc-7 g++-7 \
  && rm -rf /var/lib/apt/lists/*

# Install llvm toolchain
COPY ./apt/llvm-${VERSION}.list /etc/apt/sources.list.d/llvm.list
RUN wget --no-check-certificate -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    clang-8 \
    clang-tools-8 \
    clang-tidy-8 \
    lld-8 \
    libfuzzer-8-dev \
    libc++-8-dev \
    libc++abi-8-dev \
  && rm -rf /var/lib/apt/lists/*

ENV CC=gcc-7
ENV CXX=g++-7

# Install nebula third-party dependencies
RUN git clone --branch master --depth 1 https://github.com/vesoft-inc/nebula.git \
  && ./nebula/third-party/install-third-party.sh \
  && rm -rf nebula
