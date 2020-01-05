FROM buildpack-deps:stretch

COPY llvm.list /etc/apt/sources.list.d/
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN apt-get update && apt-get -yq install clang-7 lld-7 libc++-dev

RUN curl https://cmake.org/files/v3.8/cmake-3.8.2-Linux-x86_64.tar.gz | tar -xzf - -C /usr/local --strip-components=1
RUN apt-get update && apt-get -yq install ca-certificates ninja-build libopenal-dev libsdl2-dev libfreetype6-dev valgrind
