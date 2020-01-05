FROM ubuntu:16.04

RUN apt-get update \
      && apt-get install -y --no-install-recommends \
      software-properties-common \
      wget \
      && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
      && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0 main" \
      && apt-get update \
      && apt-get install -y --no-install-recommends \
      clang-6.0 \
      clang-format-6.0 \
      clang-tidy-6.0 \
      clang-tools-6.0 \
      lldb-6.0 \
      && rm -rf /var/lib/apt/lists/* \
      && ln -s /usr/bin/clang-6.0 /usr/bin/clang \
      && ln -s /usr/bin/clang++-6.0 /usr/bin/clang++ \
      && ln -s /usr/bin/clang-format-6.0 /usr/bin/clang-format \
      && ln -s /usr/bin/clang-tidy-6.0 /usr/bin/clang-tidy \
      && ln -s /usr/bin/lldb-6.0 /usr/bin/lldb
