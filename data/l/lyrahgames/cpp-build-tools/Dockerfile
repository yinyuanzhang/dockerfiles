from gcc:latest

label maintainer="markuspawellek@gmail.com"

arg VCS_REF
arg BUILD_DATE
label \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/lyrahgames/docker-cpp-build-tools.git"

run \
  apt-get update && \
  apt-get install -y \
    ninja-build \
    python3 \
    python3-pip \
    libboost-all-dev \
  && apt-get remove -y \
    libboost-all-dev \
  && rm -rf /var/lib/apt/lists/* \
  && pip3 install \
    meson

# install latest Boost library
workdir /tmp
run \
  git clone https://github.com/boostorg/boost.git --recursive --depth=1 --branch master --single-branch boost
workdir boost
run \
  ./bootstrap.sh && \
  ./b2 release && \
  ./b2 install
workdir /
run rm -rf /tmp/boost

# install latest CMake build system generator
workdir /tmp
run git clone https://github.com/Kitware/CMake.git --depth=1 --branch release --single-branch cmake
workdir cmake
run ./bootstrap && make && make install
workdir /
run rm -rf /tmp/cmake

# install latest fmt format library
workdir /tmp
run git clone https://github.com/fmtlib/fmt.git --depth=1 --branch master --single-branch
workdir fmt/build
run \
  cmake -D CMAKE_BUILD_TYPE=Release .. && \
  cmake --build . && \
  cmake --build . --target install
workdir /
run rm -rf /tmp/fmt