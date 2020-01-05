from gcc:latest

label maintainer="markuspawellek@gmail.com"

arg VCS_REF
arg BUILD_DATE
label \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/lyrahgames/docker-gcc-cmake.git"

workdir /tmp
run git clone https://github.com/Kitware/CMake.git --depth=1 --branch release --single-branch cmake
workdir cmake
run ./bootstrap && make && make install
workdir /
run rm -rf /tmp/cmake