FROM ubuntu:bionic
MAINTAINER Thomas Kent <docker@teeks99.com>
ARG llvmver=9

ADD llvm.list /
ADD llvm-snapshot.gpg.key /

# Pre-Req Repos
RUN apt-get update \
 && apt-get install -y software-properties-common \
  gnupg \
# Install pre-reqs
 && mv llvm.list /etc/apt/sources.list.d/ \
 && apt-key add llvm-snapshot.gpg.key \
 && rm llvm-snapshot.gpg.key \
 && apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y \
  ca-certificates \
  build-essential \
# Common Libraries
  uuid-dev \
# Install Tool
  clang-$llvmver \
  clang-tools-$llvmver \
  clang-format-$llvmver \
  clang-tidy-$llvmver \
  python-clang-$llvmver \
  libfuzzer-$llvmver-dev \
  llvm-$llvmver \
  llvm-$llvmver-tools \
  llvm-$llvmver-dev \
  liblldb-9 \
  python-lldb-9 \
#  lldb-$llvmver
  lld-$llvmver \
  libc++-$llvmver-dev \
  libc++abi-$llvmver-dev \
  libomp-$llvmver-dev \
  pkg-config \
  git-core \
 && apt-get download lldb-9 \
 && dpkg -i --ignore-depends=llvm-9-tools lldb-9_1%3a9~svn372167-1~exp1~20190917193124.56_amd64.deb
