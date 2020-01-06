FROM ubuntu:17.04
MAINTAINER Michele Adduci <info@micheleadduci.net>

VOLUME "/project"
WORKDIR "/project"

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install gcc-mingw-w64 g++-mingw-w64 cmake wget -y  && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    wget -O /tmp/conan.deb -L https://github.com/conan-io/conan/releases/download/0.25.1/conan-ubuntu-64_0_25_1.deb && \
    dpkg -i /tmp/conan.deb

ADD ./scripts/cmake-build.sh /build.sh
ADD ./cmake_toolchains/mingw.cmake /mingw.cmake

RUN chmod +x /build.sh

ENTRYPOINT exec /build.sh -DCMAKE_TOOLCHAIN_FILE=/mingw.cmake
