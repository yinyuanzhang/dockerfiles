FROM ubuntu:16.04

LABEL maintainer Mario Werner <mario.werner@iaik.tugraz.at>

# Install commonly used packages for c++ development. Additionally,
# update-alternatives is configured to simplify use of alternative tools. For
# example, using gold as default linker
#   `update-alternatives --set ld /usr/bin/ld.gold`.
#
# When ccache should be used, the path has to be extended as follows:
# `export PATH="/usr/lib/ccache:$PATH"`. Note that the default cache directory
# of ccache can be configured by exporting `CCACHE_DIR`.
RUN apt-get update && apt-get install -y \
  autoconf \
  automake \
  autopoint \
  bison \
  build-essential \
  ccache \
  clang \
  clang-format \
  clang-tidy \
  cmake \
  curl \
  doxygen \
  flex \
  gcc-multilib \
  g++-multilib \
  git \
  gperf \
  graphviz \
  lcov \
  libboost-all-dev \
  libsqlite3-dev \
  libssl-dev \
  ninja-build \
  pkg-config \
  python3 \
  python3-pip \
  valgrind \
  wget \
  && pip3 install --upgrade conan conan_package_tools \
  && update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.gold" 10 \
  && update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.bfd" 20

# Install docker to permit building images inside of the container.
# https://docs.gitlab.com/ce/ci/docker/using_docker_build.html#using-docker-build
RUN curl -sSL https://get.docker.com/ | sh

# Build and install a reasonable modern cmake version. The selected 3.10.2
# version is the same that is found in Ubuntu Bionic (18.04 LTS) and is
# therefore widely used. Still, it is already far better then the 3.5.1 version
# that can be found in Ubuntu Xenial (16.04 LTS) and Ubuntu Trusty (14.04 LTS
# via updates).
RUN git clone https://gitlab.kitware.com/cmake/cmake.git /tmp/cmake \
  && mkdir /tmp/cmake/_build \
  && cd /tmp/cmake/_build \
  && git checkout v3.10.2 \
  && ./../bootstrap --parallel=4 -- -DCMAKE_BUILD_TYPE=Release \
  && make -j4 install \
  && rm -rf /tmp/cmake
